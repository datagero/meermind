import Realm from "realm"

export class Dog extends Realm.Object {
  static schema = {
    name: "Dog",
    primaryKey: "_id",
    properties: {
      _id: { type: "objectId", default: () => new Realm.BSON.ObjectId() },
      name: "string",
      age: "int",
    },
  };
}

