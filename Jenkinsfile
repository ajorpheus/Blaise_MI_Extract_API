pipeline { 
    agent any
    stages {
        stage('PullDockerImage') {
            steps {
               sshagent(credentials: ['a069e490-f64f-47ca-b91f-61270cbd8d50']) {
                   sh '''
                   ssh -o StrictHostKeyChecking=no s_blaise5_dev@blaisedk-d-01 /bin/bash <<-INIT
                       cd ~/$WORK_DIR
                       ls
INIT
'''
               }
           }
       }
    }
}
