/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/


//sh.enableSharding("ADMdatabase")
// Select the database to use.
//use('ADMdatabase');

sh.status()

db.users.createIndex( {"user_id": 1}, {unique: true})
//db.listings.createIndex( {"listing_id": 1}, {unique: true})
db.reviews.createIndex( {"score": 1, "review_id": 1}, {unique: true})

db.listings.getShardDistribution();


/*
sh.shardCollection("ADMdatabase.users", {"user_id" :
"hashed"});
*/




// Print a message to the output window.
//console.log(`${salesOnApril4th} sales occurred in 2014.`);

