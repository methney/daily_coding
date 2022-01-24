import re

# https://blog.rhostem.com/posts/2018-11-11-regex-capture-group

string_one = 'file_record_transcript.pdf'
string_two = 'file_07241999.pdf'
string_three = 'testfile_fake.pdf.tmp'

# capturing group
pattern = '^(file.+)\.pdf$'
a = re.search(pattern, string_one)
b = re.search(pattern, string_two)
c = re.search(pattern, string_three)

# print(a.group(1) if a is not None else 'Not found')
# print(a.group())
# print(b.group(), b.group(1) if b is not None else 'Not found')
# print('not None' if c is not None else 'Not found')
# print(a)


# capturing group
pattern2 = '(?:https?:\/\/)?(\w+)\.github.com'
d= re.match(pattern2, 'https://rhostem.github.com')
# match나 search나 똑같이 결과는 나오는것 같다. 
# print(d.group()) 
# print(d.group(1))

# lookbehind
# ?<= 로 시작하는 문자열을 찾는다(https). ?<=의 문자열은 캡처링그룹에 포함시키지않는다.
pattern3 = '(?<=https):\/\/(\w+)\.github.com'
e= re.search(pattern3, 'https://rhostem.github.com')
# print(e.group())
# print(e.group(1))

# lookahead
# ?=를 포함하는 문자열의 ?= 앞부분을 리턴(캡처링그룹에 ?=는 제외)
pattern4 = '\D+(?=rhostem)'
gg= re.search(pattern4, 'https://rhostem.github.com')
print(gg.group())
# print(gg.group(1))