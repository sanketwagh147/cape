# helper script to get started with google cloud run
# prerequisites:
# - set PROJECT_ID=[your project ID] and REGION=[your region]
# - create a SQL instance
gcloud sql instances create saas_nrcapital_instance --project $PROJECT_ID --database-version POSTGRES_11 --tier db-f1-micro --region $REGION
# create database
gcloud sql databases create saas_nrcapital_db --instance saas_nrcapital_instance
# create bucket for static files
gsutil mb gs://saas_nrcapital-media
# set up secrets in secret manager
gcloud secrets create saas_nrcapital_settings --replication-policy automatic
# (create .env.production file here)
gcloud secrets versions add saas_nrcapital_settings --data-file .env.production
gcloud secrets add-iam-policy-binding saas_nrcapital_settings  --member serviceAccount:${CLOUDRUN} --role roles/secretmanager.secretAccessor
export PROJECTNUM=$(gcloud projects describe ${PROJECT_ID} --format 'value(projectNumber)')
export CLOUDBUILD=${PROJECTNUM}@cloudbuild.gserviceaccount.com
gcloud secrets add-iam-policy-binding saas_nrcapital_settings  --member serviceAccount:${CLOUDBUILD} --role roles/secretmanager.secretAccessor
gcloud projects add-iam-policy-binding ${PROJECT_ID}  --member serviceAccount:${CLOUDBUILD} --role roles/cloudsql.client
gcloud builds submit --config cloudmigrate.yaml  --substitutions _REGION=$REGION
gcloud run deploy saas-nrcapital-project --platform managed --region $REGION --image gcr.io/$PROJECT_ID/saas_nrcapital-cloudrun --add-cloudsql-instances ${PROJECT_ID}:${REGION}:saas_nrcapital_instance  --allow-unauthenticated --set-env-vars=DJANGO_SETTINGS_MODULE=saas_nrcapital.settings_production
