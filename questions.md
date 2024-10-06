# questions regarding rfc 6020

## why do we not allowed to send messages like in rfc itself, rfc normally use rpc encapsualated messages?

```xml
    <rpc message-id="101"
        xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <rock-the-house xmlns="http://example.net/rock">
        <zip-code>27606-0100</zip-code>
    </rock-the-house>
    </rpc>

    <rpc-reply message-id="101"
            xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <ok/>
    </rpc-reply>
```

# general netconf
## what nacm stands for?
# questions regarding "netconf intro a3 pdf" document
## what is the start up config duty, and what if we lack it?
## what does copy-config command does?
## what is candidate datastore, can we just write directly to running one?
## how to know if we are allowed to write to running datastore directly?
## is it possible to configure device with a file?
## what is notification in rfc 5277, how to subscribe to it, can we stop it after subscribing?
## what is partial lock in rfc 5717?


# questions regarding rfc 7950
# questions regarding rfc 8526