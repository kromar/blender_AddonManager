# blender_AddonManager

This Addon is a proof of concept, the motivation is to make a addon which can be used to download/update addons without every developer integrating a updater into their addon. All that is required for a addon to show up after it has been installed is that it is enabled and/or has a linkk to the repository in the doc_url or the bug_tracker.

The Addon is looking for tags which are considered experimental or releases for stable versions of the addon. (currenty only tested with a github proiject)
At the moment you will be directed to a download link for the addon but it should be possible to do a automatic download and update of the addons.

The concept is currently working with github and the GoB addon is there as a example. The url can be changed to try with different addon repositories.
![image](https://user-images.githubusercontent.com/1472884/140783514-91260885-78a8-49aa-8840-dee0dbbcc8de.png)
