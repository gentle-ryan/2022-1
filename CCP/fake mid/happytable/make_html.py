#
# make_html.py
#
# 실습 06 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.
#
#
# 이용할 파일을 표준입력 받아 file에 저장하여 주었습니다.

import sys
file = open(sys.argv[1])

# 첫 줄을 thread로 만들어 주었습니다.

firstline = file.readline()
thread = firstline.split(',')

# 반복되지 않은 부분은 print로 출력해주었습니다.

print("""<html><head>
    <style>
      table, th, td {
	  border: 1px solid darkgray;
	  border-collapse: collapse;
      }
      th {
	  background-color: lightgray;
      }
    </style>
  </head>
  <body data-new-gr-c-s-check-loaded="14.1057.0" data-gr-ext-installed="">
    <table style="border: 1px solid black;">
      <thead>
	<tr>""")

# 위에서 설정한 thread list 안의 요소들마다 <th> .. </th>의 형식으로 출력되도록 하였습니다.
for th in thread:
    print('<th>', th, '</th>')

print("""	</tr>
      </thead>
      <tbody>""")

# 색으로 사용할 단어들의 list를 따로 만들어주었습니다.      
colors = ['hotpink;', 'gold;', 'lightblue;', 'lightcoral;', 'limegreen;', 'orchid;', 'chocolate;']

# file의 각 줄을 ,를 기준으로 구분하여 words list를 만들어 주었습니다.
# html파일에서 1,2열은 단지 csv의 데이터가 그대로 출력이 되는 반면, 3열 부터는 div style의 color와 width가 데이터에 따라 바뀌는 것을 확인하였습니다.
# 그래서 조건문을 활용해 3개로 구분지어 작성하였습니다.
# colors list 보다 words list의 길이가 2만큼 길기 때문에 colors의 index는 words의 index에서 2만큼 빼서 사용하였습니다.
# width값은 데이터에 50배를 하라 하였으므로 float로 변환후 50을 곱해주었습니다. 
# 그런데 table.html 파일에서 width는 모두 정수값이기에 int로 변환하였으며, 문자열 'px">'와 공백 없이 이어 적기 위해 str로 변환후 이어주었습니다.   
# 한 행의 시작과 끝에 <tr></tr>이 있으므로 반복문 밖에 작성하여 주었습니다.

for line in file:
    words = line.split(',')
    print('<tr>')
    for index, word in enumerate(words):
        if index == 0:
            print('<td>', word, '</td>')
        elif index == 1:
            print('<td>', word, '</td>')
        else:
            width = str(int(float(word)*50))
            print('<td>', '<div style="background-color:', colors[index-2], 'width:', width + 'px">', word, '</div></td>')
    print('</tr>')
print("""</tbody>
    </table>
  

</body><grammarly-desktop-integration data-grammarly-shadow-root="true"></grammarly-desktop-integration></html>""")
