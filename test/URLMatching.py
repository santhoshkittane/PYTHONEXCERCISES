import tldextract


def urlmatch(str1):
    flag = True
    if str1.startswith(("http","www","https")) and str1.endswith((".com",".co.in","/")):
            pass
    else:
        flag = False
    return flag


def get_website_name(url):
    # Extract parts from the URL
    extracted = tldextract.extract(url)

    # Return just the core domain name
    return  extracted.domain.upper()


# Using a name other than 'input' to avoid overwriting the built-in function
#user_input = input("Enter String: ")
#
# if urlmatch(user_input):
#     print("URL is Valid")
# else:
#     print("URL is Invalid")

