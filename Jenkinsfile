pipeline { 
    agent any
    stages {
        stage('PullDockerImage') {
            steps {
               sshagent(credentials: ['cb4dd465-9f1b-42a5-b78b-dd3594949e3c']) {
                   sh 'ssh -o StrictHostKeyChecking=no s_blaise5_dev@blaisedk-d-01'
                   sh 'ssh -v s_blaise5_dev@blaisedk-d-01'
                   sh 'ls'
               }
           }
       }
    }
}
