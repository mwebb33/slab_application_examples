// see https://www.jenkins.io/doc/book/pipeline/shared-libraries/
@Library('dsc-shared-library')

/*
* This is a standard template some teams might want to modify this or use different Jenkins processes.
* This is a suggested pattern to follow.  Abusing the workflow described in https://confluence.silabs.com/display/DocsDev/Publish+Workflow
* could lead into delays of publishing your content in production.
* Always consult TECHPubs and DocPublishers before you build a pattern outside of this template
*/


/*
* previewMap is the mapping to the preview environments.  Please review https://confluence.silabs.com/display/DocsDev/Publish+Workflow
* These branch names should be consistent to map a release to.  Please review TECH PUB policies or reach out to a DocPublisher for more info
* Understand you cannot push to Production without pushing to Review 1st then Approve 2nd
* It is recommended that you match the Review ,Approve and Production to the same branches. May not work for all use cases
*/

def previewMap = [review: "review", approve: "approve", production: "master"]


/*
* =========================================
* should not have to update anything below
* =========================================
*/


pipeline {
    agent {label 'linux'}
    parameters {
     string defaultValue: '', description: 'Provide a Release Ticket ID if you want to move to preview.', name: 'RELEASETICKET'
    }
     options {
       buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10')
       timeout(time: 30, unit: "MINUTES")
    }
    stages {
        stage('set-up') {
            steps {
               script {
                   dsc.getSudsCLI()
               }
            }
        }
        stage('release to scratch') {
            when {
              not {
                 anyOf {
                    branch previewMap.review;
                    branch previewMap.approve;
                    branch previewMap.production
                 }
              }
            }
            steps {
               script {
                  dsc.pushScratch('production')
               }
            }
        }
        stage('release to review preview') {
            when { branch previewMap.review }
            steps {
                script {
                  dsc.pushReleasePreview('review', params.RELEASETICKET,'production')
                }
            }
        }
        stage('release to approve preview') {
            when { branch previewMap.approve }
            steps {
                script {
                  dsc.pushReleasePreview('approve', params.RELEASETICKET,'production')
                }
            }
        }
        stage('release to production preview') {
            when { branch previewMap.production }
            steps {
               script {
                  dsc.pushReleasePreview('production', params.RELEASETICKET,'production')
               }
            }
        }
        stage('cleanup') {
            steps {
                echo 'Done'
            }
        }
    }
}