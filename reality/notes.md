# Job Hunting To Do

interviewing.io

salary expectations? don't give them the number
what's the compensation band for this position?
can we revisit this later?
"that's a good start!"

javascript interview

how would you first design a static html website?
semantic html?
what is accessibility and why it matters?
what's an http request?
what's an example of different http requests?
thoughts first on mobile first with design and development?
what is specificity in CSS?
what is the box model in CSS?
implement these functions:

- add()
- add(...args)
- stringIncludes() (case sensistive)
  - toLowerCase makes a new string, doesn't manipulate the previous
    choose one
- getNames()
- getLargestNumberIndex()
- delay()

https://www.youtube.com/watch?v=vomuCMmoNyE
https://www.youtube.com/watch?v=6Wzj7kxfRdI

array.push("end")
array.unshift("start")

private variable?
function, return function, return variable
console.log(getPrivateVariable()) // super secret code
console.log(secretVariable()) // private

1: "merge request chalk line is 10 am, no more merges after that!"
2: "no more merges, no more conflicts"
3: "no more conflicts, no code"
4: "no code, no bugs"

https://www.youtube.com/watch?v=aHB8bx4P7TE

Design a reservation/payment parking garage

1. need to be able to reserve a parking spot
2. need to get a receipt for reserving
3. need to pay for parking
4. system needs high consistency (no two people should reserve at the same time)
   1. strong consistency when possible, eventual consistency if you have to
   2. strong consistency = quality over speed
   3. eventual consistency = speed over quality
5. 3 types of vehicles (compact, regular, and large)
6. flat rate, but different rates depending on parking

Public Endpoints

/reserve
params: garage_id, start_time, end_time
returns: (spot_id, reservation_id)

/payment
params: reservation_id
note: existing api to handle such as stripe, square, etc.

/cancel
params: reservation_id

Internal Endpoints

why do you want to work here?

I've always had the passion for different hobbies. Whether it be joining the Animal Crossing Community server, Mechanical Keyboard meetups, and just the traditional friend group server to play games with late at night, Discord helped with connect me with these communities. For me Discord sounds like an amazing opportunity to learn multiple technologies and absorb different perspectives from fellow co-workers.
