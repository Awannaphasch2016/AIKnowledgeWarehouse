:EC2:AWS:setup:ssh
* how to connect to ec2 via ssh
    * reference: https://medium.com/@junseopark/from-zero-to-aws-ec2-for-data-science-62e7a22d4579

    1. SSH into the EC2 instance

    `ssh -i "~/Downloads/tutorial.pem" ubuntu@ec2-3-131-36-185.us-east-2.compute.amazonaws.com`

    2. Upload data into EC2

    `scp -i <key-pair-file> <data-file> <ec2-username>@<ec2-public-dns>:<ec2-directory>`

    3. Open a Jupyter Notebook 

    `ssh -i <key-pair-file> -L <local-port>:localhost:<ec2-port> <ec2-username>@<ec2-public-dns>`

