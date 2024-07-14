
export function defineCancelApiObject(apiObject: any) {
    // an object that will contain a cancellation handler
    // associated to each API property name in the apiObject API object
    const cancelApiObject: any = {}

    // each property in the apiObject API layer object
    // is associated with a function that defines an API call

    // this loop iterates over each API property name
    Object.getOwnPropertyNames(apiObject).forEach((apiPropertyName) => {
        const cancellationControllerObject: any = { // Explicitly type cancellationControllerObject as any
            controller: undefined,
        }

        // associating the request cancellation handler with the API property name
        cancelApiObject[apiPropertyName] = {
            handleRequestCancellation: () => {
                // if the controller already exists,
                // canceling the request
                if (cancellationControllerObject.controller) {
                    // canceling the request and returning this custom message
                    cancellationControllerObject.controller.abort()
                }

                // generating a new controller
                // with the AbortController factory
                cancellationControllerObject.controller = new AbortController()

                return cancellationControllerObject.controller
            },
        }
    })

    return cancelApiObject
}