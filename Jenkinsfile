// see https://confluence.silabs.com/display/DocsDev/Jenkins+Process+Set+Up
// see https://www.jenkins.io/doc/book/pipeline/shared-libraries/
@Library('dsc-shared-library') _
 
pipeline {
    agent {label 'suds-cm-slave-spot'}
    parameters {
       string defaultValue: null, description: 'Provide a Release Ticket ID if you want to move to preview.', name: 'RELEASETICKET'
    }
    options {
       timestamps()
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
                    expression {
                        return params.RELEASETICKET
                    }
                }
            }
            steps {
               script {
                    dsc.pushScratch('production')
               }
            }
        }
        stage('release ticket found, pushing to preview-env') {
            when {
                expression {
                    return params.RELEASETICKET
                }
            }
            steps {
               script {
                    dsc.pushReleasePreview('production', params.RELEASETICKET, 'production')
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