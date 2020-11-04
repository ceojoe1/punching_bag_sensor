import processing.net.*;
Client c;

void setup() {
  size(200, 200);
  c = new Client(this, "127.0.0.1", 5000);
}

void draw() {
  println("Is available: " + c.available());
  if (c.available() > 0) {
    c.write("Paging Python!");
  }
}
