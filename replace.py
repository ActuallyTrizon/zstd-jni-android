import os

try:
    with open("./CMakeLists.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace("zstd-jni-","zstd-jni_dh-")
    with open("./CMakeLists.txt", 'w', encoding='utf-8') as f:
        f.write(new_content)
except Exception as e:
    print(e)      

dir = "./src/main/native"
for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = content.replace("com_github_luben", "dhcomgithubluben").replace("com/github/luben", "dhcomgithubluben")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            except Exception as e:
                print(e)