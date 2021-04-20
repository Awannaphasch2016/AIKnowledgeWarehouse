:EC2:AWS:basics:
    * what are types of driver for gpu nvidia? 
* list ec2 instances 
    * ref
        * https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instances.html
    * filter by instanceId
        * `aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId"` 
        * `aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId"` 
    * filter by tags
        * `aws ec2 describe-instances --filters "Name=tag:Name,Values=MyInstance"`
    * filter by others
        * `aws ec2 describe-instances --filters "Name=image-id,Values=ami-x0123456,ami-y0123456,ami-z0123456"`

:EC2:AWS:vpc:basic:
* run ec2 instances
    * run with vpc
        * `aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e`
    * run without vpc
        * `aws ec2 run-instances --image-id ami-173d747e --count 1 --instance-type t1.micro --key-name MyKeyPair --security-groups my-sg`

:EC2:AWS:vpc:basic:
* terminate ec2 instances
    * ref
        * https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instances(.html
    * `aws ec2 terminate-instances --instance-ids i-5203422c`

:EC2:AWS:key-pair:security:setup:
* create key-pair for ec2 
    * `aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > single-gpu.pem`

:EC2:AWS:setup:cli:examples:
* create aws ec2 from command line
    * `aws ec2 run-instances --image-id  ami-08962a4068733a2b6 --count 1 --instance-type p3.8xlarge --key-name
        MyKeyPair --cpu-options=CoreCount=16,ThreadsPerCore=2
        `
