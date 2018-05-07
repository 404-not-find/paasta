@Library('jenkinsfile_stdlib') _

yproperties() // Sets releng approved global properties (SCM polling, build log rotation, etc)


CHANNELS = ['paasta']
GIT_SERVER = 'git@github.com'
PACKAGE_NAME = 'mirrors/Yelp/paasta'
DIST = ['trusty', 'xenial', 'bionic']

ircMsgResult(CHANNELS) {
    ystage('Test') {
        node {
            clone(
                PACKAGE_NAME,
            )
            sh 'make itest'
        }
    }

    // Runs `make itest_${version}` and attempts to upload to apt server if not an automatically timed run
    // This will automatically break all the steps into stages for you
    debItestUpload(PACKAGE_NAME, DIST)

    ystage('Upload to PyPi') {
        node {
            promoteToPypi(
                "git@git.yelpcorp.com:mirrors/Yelp/paasta.git",
                commit,
            )
        }
    }
}
