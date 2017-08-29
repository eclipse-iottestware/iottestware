# 1 Reporting an Issue

IoT-Testware uses [GitHub Issue Tracking](https://guides.github.com/features/issues/) to track issues (primarily bugs and contributions of new code). If you've found a bug in the test purposes or the test code, this is the place to start. You'll need to create a (free) GitHub account in order to submit an issue, to comment on them or to create pull requests.

## 1.1 Creating a Issue

If you've found a problem in on of the test suites, do a search on GitHub under _Issues_ of the [related project](https://projects.eclipse.org/projects/technology.iottestware/developer) in case it has already been reported. If you are unable to find any open GitHub issues addressing the problem you found, your next step will be to open a new one.

Your issue report should contain a **title** and a **clear description** of the issue at the bare minimum. You should include as much **relevant information** as possible. Your goal should be to make it easy for yourself - and others - to reproduce the bug and figure out a fix. The same goal is appropriated to a wrongly created test purposes that needs to be discussed. Always try to rely on an official source (e.g. standard).

## 1.2 Creating a Feature or new Test Suite Request

Please don't put "feature request" items into GitHub Issues. If there's a new feature (like an additional test case that you want to see added to a dedicated test suite) or a new test suite idea, you'll need to write the code yourself - or convince someone else to partner with you to write the code. Later in this guide, you'll find detailed instructions for proposing a patch to IoT-Testware. If you enter a wish list item in GitHub Issues with no test purpose or no code, you can expect it to be marked "invalid" as soon as it's reviewed.

If you'd like feedback on an idea for a feature before doing the work to make a patch, please send an email to the [iottesware-dev list](https://dev.eclipse.org/mailman/listinfo/iottestware-dev). You might get no response, which means that everyone is indifferent. You might find someone who's also interested in building that feature. You might get a "This won't be accepted." But it's the proper place to discuss new ideas. GitHub Issues are not a particularly good venue for the sometimes long and involved discussions new features require.

# 2 Contributing to the IoT-Testware code

As a next step beyond reporting issues, you can help resolve existing issues. If you check the issues list in GitHub Issues for your interested project, you'll find issues already requiring attention.

## 2.1 Setting Up the Environment
### 2.1.1 Java
In order to run Eclipse Titan IDE (based on Eclipse IDE) you need to have the latest version of Java installed.

### 2.1.2 Git
The Eclipse Iot-Testware project uses Git for source code control. We refer to the [Git homepage](https://git-scm.com/) where you find installation instructions.

### 2.1.3 Eclipse Titan
Eclipse Titan is an essantial tool we use for the Iot-Testware project as it provides the TTCN-3 compiler and in addition comes along with an IDE. A Titan documentation package with well described installation instructions can be find in the download section on the [Eclipse Titan project page](https://projects.eclipse.org/projects/tools.titan/downloads).
The Titan core installation can be found in 

## 2.2 Clone the Repository
To be able to start working with the code, you need to clone the IoT-Testware repository (here we take the CoAP project as example):

```git
$ git clone https://github.com/eclipse/iottestware.coap.git
```

Then create a dedicated local branch:

```git
$ cd iottestware.coap
$ git checkout -b <your_branch_name>
```

It doesn't matter much what name you use, because this branch will only exist on your local computer and your personal repository on GitHub. It won't be part of the IoT-Testware Git repository.

## 2.3 Write (Test) Code
At this point you can start writing code. You're on your branch now, so you can write whatever you want to improve or extent the project. **But** if you're planning to submit your change back for inclusion in IoT-Testware, keep a few things in mind:

* Get the code right
* Use already defined util functions/helpers
* As this project provides test suites, all test cases must base on a test specification (aka test purpose)
* Test your implementation before you contribute
* Update whatever is affected by your contribution

### 2.2.1 Code Conventions
We are following the [ETSI Generic Naming Conventions](http://www.ttcn-3.org/index.php/development/naming-convention) for the TTCN-3 language.

In addition, follow this simple set of coding style conventions:
* Two spaces, no tabs (for indentation).
* No trailing whitespace. Blank lines should not have any spaces.
* Follow the conventions in the source you see used already.

## 2.4 Commit your Changes
If you feel fine with your code in your local branch you need to commit the changes to Git with:

```git
$ git commit -a
```

A well-formatted and descriptive commit message is very helpful to others for understanding why the change was made, so please take the time to write it.

A good commit message looks like this:

>Short summary (ideally 50 characters or less)
> 
>More detailed description, if necessary. It should be wrapped to
>72 characters. Try to be as descriptive as you can. Even if you
>think that the commit content is obvious, it may not be obvious
>to others. Add any description that is already present in the
>relevant issues; it should not be necessary to visit a webpage
>to check the history.
> 
>The description section can have multiple paragraphs.
> 
>Code examples can be embedded by indenting them with 4 spaces:
>
    module TestFunctions
    {
      var integer count := 0;
      ...
    }
   
> 
>You can also add bullet points:
> 
>\- make a bullet point by starting a line with either a dash (-)
>  or an asterisk (*)
> 
>\- wrap lines at 72 characters, and indent any additional lines
>  with 2 spaces for readability

## 2.5 Update your Branch
It might happen that other changes to master have happened while you were working. Keep always updated:

```git
$ git checkout master
$ git pull --rebase
```

Now reapply your patch on top of the latest changes:

```git
$ git checkout <your_branch_name>
$ git rebase master
```

No conflicts? Tests still run? Change still seems reasonable to you? Then move on.

## 2.6 Fork
Navigate to the main page of the related project and press "Fork" in the upper right hand corner. You will be asked where you want to add the fork. Normally you choose your own GitHub account.

Add the new remote to your local repository on your local machine (here we take the CoAP project as example):

```
$ git remote add mine https://github.com:<your_user_name>/iottestware.coap.git
```

Push to your remote:

```git
$ git push mine <your_branch_name>
```

You might have cloned your forked repository into your machine and might want to add the original IoT-Testware repository as a remote instead, if that's the case here's what you have to do.

In the directory you cloned your fork:

```git
$ git remote add iottestware.coap https://github.com/eclipse/iottestware.coap.git
```

Download new commits and branches from the official repository:

```git
$ git fetch iottestware.coap
```

Merge the new content:

```git
$ git checkout master
$ git rebase iottestware.coap/master
```

Update your fork:

```git
$ git push origin master
```

If you want to update another branch:

```git
$ git checkout <your_branch_name>
$ git rebase iottestware.coap/<your_branch_name>
$ git push origin <your_branch_name>
```

## 2.7 Issue a Pull Request
Navigate to the IoT-Testware project you just forked and pushed to (e.g. https://github.com/<your_user_name>) and click on "Pull Request" seen in the right panel. On the next page, press "New pull request" in the upper right corner.

Click on "Edit", if you need to change the branches being compared (it compares "master" by default) and press "Click to create a pull request for this comparison".

Ensure the changesets you introduced are included. Fill in some details about your potential patch including a meaningful title. When finished, press "Send pull request". The IoT-Testware team will be notified about your submission.

## 2.8 Iterate as Necessary
It's entirely possible that the feedback you get will suggest changes. Don't get discouraged: the whole point of contributing to an active open source project is to tap into the knowledge of the community. If people are encouraging you to tweak your code, then it's worth making the tweaks and resubmitting.

### 2.8.1 Updating Pull Request
Sometimes you will be asked to make some changes to the code you have already committed. This can include amending existing commits. In this case Git will not allow you to push the changes as the pushed branch and local branch do not match. Instead of opening a new pull request, you can force push to your branch on GitHub:

```git
$ git push origin <my_pull_request> -f
```

# 3 Feedback

You're encouraged to help improve the quality of this guide.
Please contribute if you see any typos or factual errors. 
If for whatever reason you spot something to fix but cannot patch it yourself, please open an issue.

And last but not least, any kind of discussion regarding these guidelines is very welcome in the [iottestware mailing list](https://dev.eclipse.org/mailman/listinfo/iottestware-dev).
