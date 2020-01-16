pipeline {
    agent {
        label 'CAE-Jenkins2-DH-AgentL01'
    }
    stages {
        stage('Clean Workspace') {
            steps{
                sh 'docker logout'
                cleanWs()
            }
        }
        stage('Conda Packaging') {
            agent{
                docker{
                    reuseNode true
                    label 'CAE-Jenkins2-DH-AgentL01'
                    image 'conda/miniconda3'
                    args '-u root'
                }
            }
            stages {
                stage('Pull from GitHub') {
                    steps {
                        git branch: 'Jenkins-Updates', credentialsId: 'JenkinsKey', url: 'git@github.jpl.nasa.gov:OpenCAE/MMS-Python-Adapter.git'
                    }
                }
                stage('Authenticate and Build') {
                    steps{
                        sh '''
                            sed "s/versionnumber/$packageVersion/g" -i meta.yaml
                            chmod +x build.sh && chmod +x bld.bat
                            conda install git -y
                            conda install conda-build -y
                            conda build . -c conda-forge --output-folder .
                        '''
                    }
                }
                stage('Upload to Artifactory') {
                    steps{
                        withCredentials([usernamePassword(credentialsId: '5bc254ab-3697-48fe-a6fd-3b58d97d6e32', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                            sh '''
                                conda install curl -q -y
                                curl https://$USER:$PASS@cae-artifactory.jpl.nasa.gov/artifactory/conda-release-local/noarch/mms-python-adapter-$packageVersion-0.tar.bz2 -T /opt/local/jenkins/workspace/CAE-SE/MMS-Python-Adapter/noarch/mms-python-adapter-$packageVersion-0.tar.bz2
                            '''
                        }
                    }
                }
            }
        }
    }
}
