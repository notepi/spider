def automatic_detect(url):
    '''
    @contact: ���ڼ����ҳ���룬��Ҫurllib��chardet
    @url:��������
    '''
    
    content = urllib.urlopen(url).read()    #��ȡ��ҳ����
    result = chardet.detect(content)        #�����ҳ����
    encoding = result['encoding']
    return encoding