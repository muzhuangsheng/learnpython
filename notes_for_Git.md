# Git学习笔记

## What is Git?
Git是一个分布式的版本管理系统。
每个人的电脑都是一个完整的版本库，可以在文件的不同版本间穿梭时光。

## What is GitHub?
Github充当“中转站”，是免费的远程仓库，方便多人参与同一个项目。

## How to connect to GitHub with SSH
用SSH连接GitHub可以不需要每次都输入用户名和密码。
参考[GitHub Help](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) ，直接一步一步跟着做就好。  
** Step1 **  checking for existing SSH Keys   
打开terminal，输入`ls -al ~/.ssh`
找到有id_rsa.pub和id_rsa，则直接到第三步；若找不到，则进行第二步。   
** Step2 ** generating new SSH Keys   
打开terminal，输入`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`。
然后一路按Enter，也可输入passphrase来保护私钥。   
** Step3 ** adding SSH key to the ssh-agent
打开terminal，输入`eval "$(ssh-agent -s)"`   
MacOS Sierra 10.12.2及以上版本，需要在.ssh目录中修改/新建一个config文件来自动加载keys和存passphrase。   
`vim ~/.ssh/config`
输入：   
>Host *   
   AddKeysToAgent yes   
   UseKeychain yes   
   IdentityFile ~/.ssh/id_rsa   

按esc，输入:wq，保存并退出。
Terminal中输入`ssh-add -K ~/.ssh/id_rsa`   
** Step4 ** adding the SSH key to GitHub account
复制公钥到剪贴板，`pbcopy < ~/.ssh/id_rsa.pub`。
登陆GitHub账户，点击settings，点击SSH and GPG keys，点击New SSH key或者Add SSH key,
 title里描述新key，然后将公钥张贴在下面文本框，点击Add SSH key.   
 Done!

## Git Command
`git add <file> <file>` 把工作区的操作提交到暂存区。   
`git commit -m "description"` 把暂存区的操作提交到版本库，并描述所做修改/新增，可以在多次add后一次性提交所有操作。   
`git tag <tagname>` 在最近一次commit加上tag，commit_id太复杂，tag更便于协作交流搜索。   
`git tag <tagname> commit_id` 在指定commit加上tag。    
`git show <tagname>` 显示指定tag的commit_id。   
`git tag` 显示所有tag。   
`git tag -d <tagname>`   
`git log --pretty=oneline --abbrev-commit` 用一行显示缩写commit_id的方式查询近期commit。  
`git checkout -b <branch_name>`创建新的branch并移到新branch工作。   
`git checkout <branch_name>` 移到指定branch。     
`git branch` 查看所有branch，当前branch会用*标识。  
`git merge <branch_name>` 将指定branch与当前branch合并。   
`git checkout -d <branch_name>` 删除指定branch。       
`git push origin <branch_name>` 将指定branch的版本库推送至远程库。   
`git pull` 将远程库新的修改拉到本地库，与GitHub中pull request相对。pull request是你clone他人库后想要对方接受你的修改而发出的请求。
pull命令则是作为库的主人收到他人pull request后查看他人的修改做的指令。查看后可以本地操作，再push到远程库。   
