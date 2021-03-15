# SeizureSaviour

## Inspiration
About 3.4 million people in the United States suffer from Epilepsy.  Epilepsy is a disorder in which nerve cell activity in the brain is disturbed, causing seizures.  One of the primary causes of these photosensitive seizures are due to viewing video content that have fast changing colors of strobing lights or fast-paced graphics. Often such video content contains "Seizure Warnings" but no measures have been taken to actually prevent these seizures in people suffering from Photosensitive Epilepsy. 

## What it does
Our application works on top of YouTube videos and intelligently masks out portions of videos containing seizure-causing content. 

## How we built it
The application utilizes a chrome extension that activates on pages containing  YouTube videos. The metadata of the video is sent to our backend server where the properties of the video are analyzed and we use Azure AI Anomaly Detector to obtain the points in the video where the luminance of the video changes rapidly over time. We then aggregate these anomalies into blocks on time where the censoring must occur. The Chrome extension then overlays a filter or mask on top of the video to perform the censoring. 

## Challenges we ran into
At first, the raw luminance data that we obtained from videos did not suffice to get results from the Anomaly Detector as expected. We spent hours experimenting with various post-processing techniques on the raw data until we settled on the one the anomaly detector worked well on. 
Since we did not have any prior experience with building chrome extensions, it was pretty challenging for us to get one to work. 

## Accomplishments that we're proud of
Successful completion of our application felt like a good contribution to the community suffering from Epilepsy. We hope that with this application, the internet would be a safer place for more people. Especially with the world transitioning to the internet in the last year due to the pandemic, we wanted to do our bit to make it safer for everyone. 

## What we learned
We dug into research papers whose topics ranged from flashing light detection to managing epilepsy. We learned a lot about the Azure API and its capabilities and about building chrome extensions, image processing techniques, cross-origin resource sharing, and full-stack development. 

## What's next for SeizureSaviour
Since we are able to obtain the periods of seizure causing content,  we can develop deep learning networks that can counteract the color changes while preserving the actual content of the video. This would enable a seamless viewing experience for our target audience. 
