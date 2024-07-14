import { api } from "./configs/axiosConfigs"
import { defineCancelApiObject } from "./configs/axiosUtils"

export const NotesAPI = {
//   get: async function (id, cancel = false) {
//     const response = await api.request({
//       url: `/products/:id`,
//       method: "GET",
//       // retrieving the signal value by using the property name
//       signal: cancel ? cancelApiObject[this.get.name].handleRequestCancellation().signal : undefined,
//     })

//     // returning the product returned by the API
//     return response.data.product
//   },
  getAll: async function (cancel = false) {
    const response = await api.request({
      url: "/get-notes",
      method: "GET",
      signal: cancel ? cancelApiObject[this.getAll.name].handleRequestCancellation().signal : undefined,
    })

    return response
  },
//   search: async function (name, cancel = false) {
//     const response = await api.request({
//       url: "/products/search",
//       method: "GET",
//       params: {
//         name: name,
//       },
//       signal: cancel ? cancelApiObject[this.search.name].handleRequestCancellation().signal : undefined,
//     })

//     return response.data.products
//   },
  create: async function (transcript : File, cancel = false) {

    let bodyFormData = new FormData();
    bodyFormData.append('files', transcript);
    bodyFormData.append('module_name', transcript.name);

    await api.request({
      url: `/upload`,
      method: "POST",
      data: bodyFormData,
      headers: { "Content-Type": "multipart/form-data" },
      signal: cancel ? cancelApiObject[this.create.name].handleRequestCancellation().signal : undefined,
    })
  },
}

// defining the cancel API object for ProductAPI
const cancelApiObject = defineCancelApiObject(NotesAPI)