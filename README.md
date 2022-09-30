
## Introduction

A starter API services (Skeleton) using Python Flask and Flask Cors to proxify original API endpoints making cross-origin AJAX possible; quick way to solve APIs that have Cross Origin Resource Sharing (CORS) issue.

In this skeleton app, it proxify the GWSAMPLE_BASIC OData of ES5 Gateway system, but technically you could proxify any API endpoints.
This code deployable to SAP BTP Cloud Foundry environment.


## Instructions

Do `git clone` this repository, you should have `cf-flask-cors-proxy` folder.

Navigate to `cf-flask-cors-proxy` folder, and edit `app.py` file; replace `<Insert Encoded Credentials>` with your encoded credentials for ES5 Gateway system.

Note: If you don't have a SAP Gateway Demo System account, you can create one [here](https://developers.sap.com/tutorials/gateway-demo-signup.html).


#### # Cloud Foundry Deployment

Login to your BTP Cloud Foundry account.

```
$ cd cf-flask-cors-proxy
$ cf push
```

Navigate to `CF App Route URL` to access the REST APIs.

> Additional notes: 
>
> * Above deployment approach is using Cloud Foundry CLI to deploy an application in the Cloud Foundry environment.
> You can find out how to get and use the Cloud Foundry command line interface [here](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/2f1d4abd0f9f4760a301f43513d2efa6.html), or [here](https://docs.cloudfoundry.org/cf-cli/).
> * For using SAP BTP cockpit to deploy application in the Cloud Foundry environment, please refer to this guide [here](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/09fdb9bdc6804c479d634297f1d07e09.html).


#### # Run on Local Machine

Do `git clone` this repository, you should have `cf-flask-cors-proxy` folder.

```
$ cd cf-flask-cors-proxy
$ pip install -r requirements.txt
$ python app.py
```

Example of REST API endpoints:

```
http://localhost:5000/ -- GWSAMPLE_BASIC

http://localhost:5000/BusinessPartnerSet  -- GWSAMPLE_BASIC/BusinessPartnerSet?$format=json
```
