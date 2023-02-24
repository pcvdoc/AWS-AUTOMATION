# EC2 Advanced Automation

Welcome to the EC2 Advanced Automation folder in my AWS Automation Scripts repository! In this folder, you'll find scripts that automate the deployment and configuration of EC2 instances and VPCs on AWS.

## What's in the Folder?

The folder contains two types of files that you can use to automate your AWS tasks:

- **Manual Install Script**: The first file in this folder is a `.txt` file that contains instructions on how to manually install WordPress on an EC2 instance. While this method can be useful for learning purposes, it can be time-consuming and prone to human error.

- **CloudFormation Template**: The second file in this folder is a `.yaml` file that contains a CloudFormation template for creating a VPC and its subnets, and then installing WordPress on an EC2 instance. This method is fully automated and can save you time and effort.

## How to Use the Files?

To use the manual install script, simply open the `.txt` file and follow the instructions. This will guide you through the process of installing WordPress on an EC2 instance manually.

To use the CloudFormation template, you'll need to have an AWS account and the necessary permissions to create and manage resources. Once you have these, you can deploy the CloudFormation stack by following these steps:

1. Open the CloudFormation console in the AWS Management Console.

2. Choose "Create stack" and select "With new resources (standard)".

3. Upload the `.yaml` file and follow the prompts to configure the stack.

4. Review the stack settings and choose "Create stack" to launch the CloudFormation stack.

Once the stack is launched, it will automatically create a VPC and its subnets, launch an EC2 instance, and install WordPress on the instance using userdata.

## Conclusion

Thank you for checking out the EC2 Advanced Automation folder in my AWS Automation Scripts repository! I hope you find these scripts useful and that they help you automate your AWS tasks. If you have any feedback or suggestions, please let me know. And don't forget to give this repository a star if you find it helpful! 😃
