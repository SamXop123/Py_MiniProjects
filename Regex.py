import re

# ---------------------------------------------------------------------------
# COMPLETE PYTHON REGEX DEMO FILE
# This file demonstrates every major regex concept, metacharacter, and method.
# Run this file to see outputs for all regex patterns in one place.
# ---------------------------------------------------------------------------

print("\n=========================")
print("  REGEX: DIGIT MATCHING  ")
print("=========================\n")

print(re.findall(r"\\d", "A1B2C3"))                # Digits
print(re.findall(r"\\D", "A1B2C3"))                # Non-digits

print("\n==============================")
print("  REGEX: WHITESPACE MATCHING  ")
print("==============================\n")

print(re.findall(r"\\s", "Hi Sam"))               # Whitespace
print(re.findall(r"\\S", "Hi Sam"))               # Non-whitespace

print("\n==============================")
print("  REGEX: WORD MATCHING         ")
print("==============================\n")

print(re.findall(r"\\w", "Sam_123!"))             # Word chars
print(re.findall(r"\\W", "Sam_123!"))             # Non-word chars

print("\n=======================")
print("  DOT CHARACTER '.'    ")
print("=======================\n")

print(re.findall(r".", "Hi!"))                     # Any character except newline

print("\n=======================")
print("  QUANTIFIERS * + ?     ")
print("=======================\n")

print(re.findall(r"ap?ple", "apple aple"))         # ? zero/one
print(re.findall(r"a+", "aaa bb a"))               # + one/more
print(re.findall(r"ho*", "h ho hoo"))              # * zero/more

print("\n======================")
print("  WORD BOUNDARY \\b   ")
print("======================\n")

print(re.findall(r"\\bcat", "cat catalog"))       # boundary
print(re.findall(r"cat\\b", "my cat is cool"))     # boundary end

print("\n======================")
print(" CHARACTER CLASSES []  ")
print("======================\n")

print(re.findall(r"[abc]", "a1b2c3d4"))            # any of a,b,c
print(re.findall(r"[^abc]", "abcXYZ"))             # NOT a,b,c

print("\n======================")
print(" SPECIAL CHAR ESCAPES  ")
print("======================\n")

print(re.findall(r"\\.", "www.google.com"))       # literal dot
print(re.findall(r"\\*", "a*b"))                  # literal asterisk

print("\n======================")
print(" RANGE QUANTIFIER {}   ")
print("======================\n")

print(re.findall(r"\\d{2,4}", "1 22 333 4444 55555"))

print("\n======================")
print("   ALTERNATION |       ")
print("======================\n")

print(re.findall(r"cat|dog", "cat dog tiger"))

print("\n======================")
print("   GROUPS AND ()       ")
print("======================\n")

print(re.findall(r"(ab)+", "ababab xyz"))           # capturing group repeat
print(re.findall(r"(cat|dog)", "cat dog tiger"))     # OR inside group

print("\n======================")
print("   NON-CAPTURING (?:)  ")
print("======================\n")

print(re.findall(r"(?:ab)+", "ababab xyz"))         # same as above but non-capturing

print("\n=============================")
print("   LOOKAHEAD (?=) (?!)      ")
print("=============================\n")

print(re.findall(r"Sam(?=123)", "Sam123 Sam456"))   # Sam followed by 123
print(re.findall(r"Sam(?!123)", "Sam123 Sam456"))   # Sam NOT followed by 123

print("\n=============================")
print("   LOOKBEHIND (?<=) (?<!)    ")
print("=============================\n")

print(re.findall(r"(?<=Mr )[A-Za-z]+", "Mr Sam and Mr John"))   # word after 'Mr '
print(re.findall(r"(?<!Mr )Sam", "Mr Sam and Sam"))             # Sam NOT preceded by Mr

print("\n=============================")
print("   START ^ and END $         ")
print("=============================\n")

print(re.findall(r"^Hello", "Hello World"))          # start
print(re.findall(r"World$", "Hello World"))          # end

print("\n=============================")
print("   MULTILINE MODE (re.M)      ")
print("=============================\n")

text = "Hello\nWorld\nPython"
print(re.findall(r"^\w+", text, re.M))              # match start of each line

print("\n=============================")
print("   DOTALL MODE (re.S)         ")
print("=============================\n")

print(re.findall(r"A.*Z", "A---\n---Z", re.S))        # dot includes newline

print("\n=============================")
print("   re.match() examples        ")
print("=============================\n")

m = re.match(r"Hi", "Hi Sam")
print(m.group())

print(re.match(r"Hi", "Sam Hi"))   # None

print("\n=============================")
print("   re.search() examples       ")
print("=============================\n")

print(re.search(r"Hi", "Sam Hi").group())

print("\n=============================")
print("   re.findall() examples      ")
print("=============================\n")

print(re.findall(r"\\d", "a1b2c3"))

print("\n=============================")
print("   re.split() examples        ")
print("=============================\n")

print(re.split(r"\\s+", "Sam is learning regex"))

print("\n=============================")
print("   re.sub() examples          ")
print("=============================\n")

print(re.sub(r"\\d", "X", "a1b2c3"))

print("\n=============================")
print("   FULLMATCH example          ")
print("=============================\n")

print(re.fullmatch(r"\\d{3}", "123"))
print(re.fullmatch(r"\\d{3}", "1234"))

print("\n=============================")
print("  EMAIL VALIDATION EXAMPLE    ")
print("=============================\n")

pattern = r"^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,6}$"
emails = ["sam123@gmail.com", "hello@xyz.in", "bad@.com"]

for e in emails:
    print(e, "=>", bool(re.match(pattern, e)))

print("\n=============================")
print(" PASSWORD VALIDATION EXAMPLE  ")
print("=============================\n")

password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{8,}$"
passwords = ["Sam@1234", "weakpass", "HELLO123!", "StrongPass@99"]

for p in passwords:
    print(p, "=>", bool(re.match(password_pattern, p)))

print("\n=============================")
print(" ALL REGEX DEMOS COMPLETED    ")
print("=============================\n")
