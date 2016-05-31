def automatic_detect(url):
    '''
    @contact: ÓÃÓÚ¼ì²âÍøÒ³±àÂë£¬ĞèÒªurllib£¬chardet
    @url:ÊäÈëÁ´½Ó
    '''
    
    content = urllib.urlopen(url).read()    #¶ÁÈ¡ÍøÒ³ÄÚÈİ
    result = chardet.detect(content)        #¼ì²âÍøÒ³±àÂë
    encoding = result['encoding']
    return encoding