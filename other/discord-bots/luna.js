const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('./settings.json') // ./ = current directory

client.on('ready',() => {
    console.log(`Logged in as ${client.user.tag}!`);
})

var prefix = "Luna, "
client.on('message', message => {
    if (message.author === client.user) return;
    if (message.content.startsWith(prefix)) {
        if (message.content === 'hello') {
            message.channel.send('Hello there master, hope all is well.');
        }

        if (message.content === 'how are you?') {
            message.channel.send('Fine, thank you.');
        }

        if (message.content === 'Luna, pi please') {
            message.channel.send(`3.14159265359... there's more, but I'd rather not finish. :tired_face:`);
        }
    }
})

client.login(settings.token);