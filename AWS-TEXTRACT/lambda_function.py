import json
import boto3
from io import StringIO
from parser import (
    extract_text,
    map_word_id,
    extract_table_info,
    get_key_map,
    get_value_map,
    get_kv_map,
)


def lambda_handler(event, context):
    textract = boto3.client("textract")
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj["s3"]["bucket"]["name"])
        filename = str(file_obj["s3"]["object"]["key"])

        print(f"Bucket: {bucketname} ::: Key: {filename}")

        response = textract.analyze_document(
            Document={
                "S3Object": {
                    "Bucket": bucketname,
                    "Name": filename,
                }
            },
            FeatureTypes=["FORMS", "TABLES"],
        )

        print(json.dumps(response))

        raw_text = extract_text(response, extract_by="LINE")
        word_map = map_word_id(response)
        table = extract_table_info(response, word_map)
        key_map = get_key_map(response, word_map)
        value_map = get_value_map(response, word_map)
        final_map = get_kv_map(key_map, value_map)

        print(json.dumps(table))
        print(json.dumps(final_map))
        print(raw_text)

        # Move the processed file to the "done" folder
        new_filename = "done/" + filename.split("/")[-1]
        s3.copy_object(Bucket=bucketname, CopySource=bucketname + "/" + filename, Key=new_filename)
        s3.delete_object(Bucket=bucketname, Key=filename)

        # Find specified keys and their values
        keys = [
        "GARANZIA FIDEIUSSORIA",
        "Garanzia fideiussoria n.",
        "Contraente (Obbligato Principale):",
        "C.F./P.IVA",
        "Stazione appaltante (Beneficiario)",
        "Codice CIG",
        "Data presentazione offerta",
        "Somma garantita",
        "CONTRAENTE",
        "C.F.",
        "P.IVA",
        "STAZIONE APPALTANTE",
        "Data Presentazione Offerta",
        "DESCRIZIONE CONTRATTO",
        "Somma Garantita",
        "Premio Netto",
        "Accessori",
        "Imposte",
        "Imponibile",
        "Premio finito"
        ]

        output = {}
        for key in keys:
            if key in final_map:
                output[key] = final_map[key]
                
         # Save the extracted table as a JSON file
        if table:
            table_filename = "done/" + filename.split("/")[-1].replace(".pdf", "_table.json")
            table_json = json.dumps(table)
            s3.put_object(Bucket=bucketname, Key=table_filename, Body=table_json)

        # Upload the JSON file to the "done" folder
        json_file = json.dumps(output)
        s3.put_object(Bucket=bucketname, Key=new_filename.replace(".pdf", ".json"), Body=json_file)

    return {"statusCode": 200, "body": json.dumps("Thanks from Srce Cde!")}
