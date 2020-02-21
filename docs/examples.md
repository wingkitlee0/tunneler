AWS Example

```
ssh -i [your-private-key.pem] -N -f -L 8888:localhost:8888 ubuntu@[ec2-ip-address-from-amazonaws.com]
```

Note:
- need to create a security group that allows TCP inbound rule at port 8888 (or other port number)