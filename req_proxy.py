from requests import Session


class GetReq(object):
    def __init__(self,proxy=True,proxy_type=True,ip_p=str(),user_p=str(),pasw_p=str(),port_p=int()) -> None:
        self.req = Session()
        self.proxy = proxy
        self.proxy_type = proxy_type

        self.ip_p = ip_p
        self.user_p = user_p
        self.pasw_p = pasw_p
        self.port_p = port_p



    def getreq_GET(self,url,header):
        if self.proxy == True:
            if self.proxy_type == True:#http
                self.proxy_statement = {'http' : 'http://{}:{}@{}:{}'.format(self.user_p,self.pasw_p,self.ip_p,self.port_p) }
            if self.proxy_type == False:#sock5
                self.proxy_statement = {'socket5' : 'socket5://{}:{}@{}:{}'.format(self.user_p,self.pasw_p,self.ip_p,self.port_p) }

            status = self.req.get(url=url,proxies=self.proxy_statement,headers=header,timeout=10)
        
            traffic = len(status.content) / 1024
            #print(traffic)
            if status.status_code == int(200):
                self.req.close()
                return status,traffic
        if self.proxy != True:

            status = self.req.get(url=url,timeout=10)
            traffic = len(status.content) / 1024
            #print(traffic)
            if status.status_code == int(200):
                self.req.close()
                print(status)
                return status,traffic


    def getreq_POST(self,url,header,data):
        if self.proxy == True:
            if self.proxy_type == True:#http
                self.proxy_statement = {'http' : 'http://{}:{}@{}:{}'.format(self.user_p,self.pasw_p,self.ip_p,self.port_p) }
            if self.proxy_type == False:#sock5
                self.proxy_statement = {'socket5' : 'socket5://{}:{}@{}:{}'.format(self.user_p,self.pasw_p,self.ip_p,self.port_p) }
            status = self.req.post(url=url,proxies=self.proxy_statement,headers=header,data=data,timeout=10)
            traffic = len(status.content) / 1024
            #print(traffic)
            if status.status_code == int(200):
                self.req.close()
                return status,traffic
        if self.proxy != True:
            status = self.req.post(url=url,headers=header,data=data,timeout=10)
            traffic = len(status.content) / 1024
            #print(traffic)
            if status.status_code == int(200):
                self.req.close()
                return status,traffic


    

    def conn_close(self):
        self.req.close()


#obj = GetReq(proxy=True,proxy_type=True,ip_p=<>,user_p=<>,pasw_p=<>,port_p=<>)