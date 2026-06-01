# Ripple Client

A Discord alternative that I'm writing because I want to get better at full stack and I hate Discord.
I also want to do some privacy/security stuff with it.

## To-do

* Setup project issues to track work more effectively
* Hook frontend/backend for server channel navigation and displaying messages in channel
* Build the actual server (this is the client) and make a connection with it

## Tech I'm Looking At

I eventually want to look at privacy and security implementations for sending messages back and forth through a trusted 3rd party server (similar to the Signal protocol, but on a larger scale). To that end, I'm investigating some technologies I'm unfamiliar with as research:

* [RaptorQ Forward Error Correction](https://datatracker.ietf.org/doc/html/rfc)
* [Messaging Layer Security (MLS) Protocol](https://datatracker.ietf.org/doc/html/rfc9420)
* [Reed-Solomon Error Correction](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)

## Building

`pnpm install`

`pnpm tauri dev`

## Contributing

If you have any ideas as to what might be useful for a more privacy focused Discord alternative, feel free to contact me! I'm not really taking pull requests/issues from the public at the moment though until there's an official release.

## License

This project is not licensed, I don't really care what you do with the code you find here.
