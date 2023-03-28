import openai
from stackapi import StackAPI
import os
import time
from datetime import datetime, timedelta
import random
import pytz

seoul_tz = pytz.timezone('Asia/Seoul')
now = datetime.now(seoul_tz)
# Create a StackAPI object for the Stack Overflow site
print('#####################################################################')
# print('sk-iqaso9waIWt13kEszXtST3BlbkFJuTCS4vx0r4UWTJDZPDgc1yoouoo')
print(now)
SITE = StackAPI('stackoverflow')
one_year_ago = (datetime.utcnow() - timedelta(days=365)).strftime('%Y-%m-%d')

# Random하게 tag선택
tag_list = ['javascript', 'typescript',
            'reactjs', 'html', 'css', 'nestjs', 'nodejs']
selected_tag = random.choice(tag_list)
print(f'카테고리는 {selected_tag} 로 하겠습니다.')
try:
	# Fetch the 10 most popular questions with the tag
	questions = SITE.fetch('questions', pagesize=20, fromdate=one_year_ago, sort='votes', order='desc', tagged=selected_tag)

	# Check if there are any questions in the response
	if not questions['items']:
	    print("No questions found.")
	    os.exit()
	    print("프로그램 강제 종료.")
	else:
	    # 0 ~ 50 한 개만 선택
	    question = questions['items'][random.randint(0, 100)]
	    topic = question['title']
	    tags = question['tags']
	    print(f'주제는 {topic} 로 하겠습니다.')
except Exception as e:
	print("StackAPI 오류발생 : ", e)
	raise SystemExit("프로그램 종료.")

# (/[`~!@#$%^&*|\\\'\";:\/?]/gi, "");
openai.api_key = os.environ.get('OPEN_API_KEY')


def generate_response(prompt, max_tokens, temperature):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,      # creativity
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion


def generate_blog_to_title(topic):
    prompt = f'''
    {topic} is about an error in "https://stackoverflow.com/". 
    Read it and replace it with the appropriate title.
    Do not use like "Blog title: ", just give me a title
    '''
    return generate_response(prompt, max_tokens=100, temperature=0.2)


def generate_blog_common_error(title):
    prompt = f'''
    {title} is a question about what error.
    Write a subheading at the top for what you're going to write about.
    Generate an article about {title}, but do not include any conclusions or summaries in your response.
    Please stop generating text when you encounter the words "Conclusion" or "Summary" or "In conclustion" or "In summary".
    Write down at least two common mistakes or why you're getting these errors.
    Use Highlight, Bold, Italic and Apostrophe for Emphasis to keywords.
    Put the javascript or typescript code to make it easier to understand in the middle of the description.
    And explain each example in code as long as possible.
    Write that code using language with related to error.
    Make it at least 10 paragraphs long, the average person would have to read for 20 minutes.
    The people reading this are developers in their 20s and 30s, so we need to explain it with code based.
    All posts should be written in markdown format.
    '''
    return generate_response(prompt, max_tokens=2500, temperature=0.5)

# 에러 해결방법 생성


def generate_blog_error_body(title):
    prompt = f'''
    I need a error handling blog post.
    {title} is the title of the question about what error.
    Skip the title and go straight to the body of the post.
    Use Highlight, Bold, Italic and Apostrophe for Emphasis to keywords.
    When it comes to this error, Write in such detail that people will see this and all the errors will be resolved.
    Write a step-by-step solution to this error.
    Put the javascript or typescript code to make it easier to understand in the middle of the description.
    And explain each example in code as long as possible.
    The people reading this are developers in their 20s and 30s, so we need to explain it with code based.
    Make it at least 20 paragraphs long, the average person would have to read for 35 minutes.
    All posts should be written in markdown format.
    '''
    return generate_response(prompt, max_tokens=2500, temperature=0.5)

# 참고 할만한 홈페이지


def generate_blog_recommend_site(title):
    prompt = f'''
    Recommend a few official sites to read about {title}.
    At the top, write the title "Recommended sites".
    Write it in MD format, leaving only the URL address.
    Refer users to sites that don't have 404 errors when they visit. A site that is actually usable.
    '''
    return generate_response(prompt, max_tokens=400, temperature=0.5)


try:
	# 제목 생성
	title_response = generate_blog_to_title(topic)
	title = '\n'.join(
	    title_response['choices'][0]['text'].strip().split('\n')[:])
	print(f"제목 만들었습니다. {title} :",
	      title_response["usage"]["total_tokens"])
except Exception as e:
        print("제목 오류발생 : ", e)
        raise SystemExit("프로그램 종료.")

try:
	# 본문 생성
	common_error_response = generate_blog_common_error(title)
	common_error = '\n'.join(
	    common_error_response['choices'][0]['text'].strip().split('\n')[1:])
	print("본문 1/2 만들었습니다. :",
	      common_error_response["usage"]["total_tokens"])

	error_body_response = generate_blog_error_body(title)
	error_body = '\n'.join(
	    error_body_response['choices'][0]['text'].strip().split('\n')[1:])
	print("본문 2/2 만들었습니다. :",
	      error_body_response["usage"]["total_tokens"])
except Exception as e:
        print("본문 오류발생 : ", e)
        raise SystemExit("프로그램 종료.")

try:
    # 참고할만한 사이트
    recommend_site_response = generate_blog_recommend_site(title)
    recommend_site = '\n'.join(
        recommend_site_response['choices'][0]['text'].strip().split('\n')[:])
    print(f"참고할만한 사이트를 만들었습니다. {title} :",
          recommend_site_response["usage"]["total_tokens"])
except Exception as e:
    print("참고할만한 사이트 생성 오류 발생 : ", e)
    raise SystemExit("프로그램 종료.")

# 어제 일자 생성
yesterday = datetime.now() - timedelta(days=1)

timestring = yesterday.strftime('%Y-%m-%d')

title = title.replace('"', '')
filename = f"{timestring}-{'-'.join(title.lower().split())}.md"

page_outline = f'''---
layout: post
title: "{title}"
tags: {tags}
---
'''

output = page_outline + '\n' + \
    "![Image of a Cat](http://source.unsplash.com/1600x900/?cat)" + \
    '\n' + common_error + '\n' + error_body + '\n' + recommend_site

print("파일을 생성하기 전 잠깐 기다립니다.")
blog_directory = "/home/yoon/blog/1yoouoo.github.io/_posts"

time.sleep(2)
# 파일 이름 생성
filepath = os.path.join(blog_directory, filename)

try:
    print("파일을 생성하겠습니다.")
    with open(filepath, 'w') as f:
        f.write(output)
        f.close()
except Exception as e:
    print("파일 생성 오류 발생 : ", e)
    raise SystemExit("프로그램 종료.")

print("모든 작업이 끝났습니다.")
print('#####################################################################')
