import subprocess
# feel free to add more so as to fine tune results
def lets_wget_it(link):
    subprocess.run([
        "torsocks",
        "wget",
        "--recursive",                   # process the supplied url and each path it includes
        "--mirror",                      # downloads entire site
        "--convert-links",               # makes all the links to work properly with the offline copy
        "--page-requisites",             # download JS and CSS files to retain the original page style when browsing a local mirror
        "--adjust-extension",            # adds proper extensions to filenames
        "--wait=1",                      # time intervals between each request
        "--random-wait",                 # randomizing the wait time to mimic human behaviour
        "--no-check-certificate",        # bypass ssl checks
        "-P Mirror",                     # dir for saving the files
        "-e robots=off",                 # control the crawling
        link
    ])
