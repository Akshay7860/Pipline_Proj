node {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')



        stage 'Deploy'
            sh '/home/ubuntu/deploy_prod.sh'

    }


