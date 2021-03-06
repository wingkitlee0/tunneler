import os
import argparse

def isIPaddress(ip):
    ip_ = ip.split(".")
    if len(ip_) == 4:
        ip_ = [ 0 <= int(d) < 256 for d in ip_] # create a list of boolean
        return all(ip_)
    else:
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-p", type=int, default=8889, help="port number to tunnel")
    parser.add_argument("-u", type=str, default=None, help="username")
    parser.add_argument("-ip", type=str, help="ip address or a text file with the ip address. \nDefault: read from TUNNELER_DEFAULT_IP env. variable")
    args = parser.parse_args()

    if args.u is None:
        args.u = ""
    else:
        args.u += "@"
    
    if args.ip is None:
        args.ip = os.environ['TUNNELER_DEFAULT_IP']
        print("Using default IP: ", args.ip)
      
    if isIPaddress(args.ip):
        cmdline = "ssh -N -f -L localhost:%i:localhost:%i %s%s" % (args.port, args.port, args.u, args.ip)
    else:
        cmdline = "ssh -N -f -L localhost:%i:localhost:%i %s$(cat %s)" % (args.port, args.port, args.u, args.ip)

    print("Running: ", cmdline)
    os.system(cmdline)
    
if __name__=='__main__':
    main()