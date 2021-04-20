:kinsis:aws:cli:shard:
* list stream 
    * ref
        * https://docs.aws.amazon.com/cli/latest/reference/kinesis/list-streams.html
    * `aws kinesis list-streams`

* list shard iterator
    * ref
        * https://docs.aws.amazon.com/cli/latest/reference/kinesis/list-shards.html 
    * `aws kinesis list-shards \
    --stream-name samplestream \
    --exclusive-start-shard-id shardId-000000000000`

* get shard iterator
    * ref 
        * https://docs.aws.amazon.com/cli/latest/reference/kinesis/get-shard-iterator.html
    * `aws kinesis get-shard-iterator \
    --stream-name samplestream \
    --shard-id shardId-000000000001 \
    --shard-iterator-type LATEST`

* get records
    * ref 
        * https://docs.aws.amazon.com/cli/latest/reference/kinesis/get-records.html
    `aws kinesis get-records \
        --shard-iterator
        AAAAAAAAAAF7/0mWD7IuHj1yGv/TKuNgx2ukD5xipCY4cy4gU96orWwZwcSXh3K9tAmGYeOZyLZrvzzeOFVf9iN99hUPw/w/b0YWYeehfNvnf1DYt5XpDJghLKr3DzgznkTmMymDP3R+3wRKeuEw6/kdxY2yKJH0veaiekaVc4N2VwK/GvaGP2Hh9Fg7N++q0Adg6fIDQPt4p8RpavDbk+A4sL9SWGE1`
