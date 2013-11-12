.. code-block:: ini

    [ec2]
    key_filename = /path/to/your/ssh/my_key
    ami_id = ami-XYZ
    api_wait = 10
    ; int. see boto.ec2.regions
    region = 5
    security_groups = webserver
