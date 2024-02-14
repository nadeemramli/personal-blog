# Get Started

`git clone https://github.com/jackyzha0/quartz.git`\
`cd quartz`\
`npm i`\
`npx quartz create`

# Building your Quartz

`npx quartz build --serve`

# Syncing Content

`npx quartz sync --no-pull`

In future updates, you can simply run `npx quartz sync` every time you want to push updates to your repository.


# Updating my Quartz

`npx quartz update`

Resolves any unmerged manually, can use `git add <path of unmerged files>`

Commit changes 

Restore changes/stash/backup

`git restore .`

Double check with  `npx quartz build --serve`

If all good, push to `git push origin v4`


## Resources

[Configuration Quartz](https://quartz.jzhao.xyz/configuration)\
[Editing Quartz](https://quartz.jzhao.xyz/layout)
