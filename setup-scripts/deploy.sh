gcloud builds submit \
    --tag $GOOGLE_CLOUD_REGION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/superset-repository/superset src/.;
    
gcloud run deploy superset \
    --image=$GOOGLE_CLOUD_REGION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/superset-repository/superset:latest \
    --allow-unauthenticated \
    --port=8088 \
    --cpu=2 \
    --memory=4096Mi \
    --min-instances=0 \
    --max-instances=1 \
    --set-secrets=CONNECTION_STRING=superset-connection-string:latest,SECRET_KEY=superset-secret-key:latest,GOOGLE_ID=google-client-id:latest,GOOGLE_SECRET=google-client-secret:latest \
    --set-cloudsql-instances $SUPERSET_CONNECTION_NAME \
    --platform=managed \
    --service-account superset@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com \
    --region=$GOOGLE_CLOUD_REGION;