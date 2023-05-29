 from GoogleNews import GoogleNews
 import time



def Scrapper(str1):
  gn = GoogleNews()
 gn.search(str1)
 result=[]
 time.sleep(5)

count=0

  for i in range(1,11):
      gn.get_page(i)
      result.append(gn.results())
    


  for j in result[0]:
     count=count+1
     print(j)
     print(count)
     print()

    return result[0]
