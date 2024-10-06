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

# questions regarding rfc 7950
# questions regarding 