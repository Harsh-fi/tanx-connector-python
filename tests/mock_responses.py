list_deposits_response = {
    "status": "success",
    "message": "",
    "payload": {
        "count": 493,
        "next": "",
        "previous": None,
        "results": [
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Pending",
                "brine_deposit_status": "Pending",
                "deposit_blockchain_hash": "0x6dacf57358e59018d5202e78ea5fb5a81ccd8741c524ca712e16f14e55b31ec2",
                "amount": "100",
                "created_at": "2023-08-07T04:29:57.732857Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Pending",
                "brine_deposit_status": "Pending",
                "deposit_blockchain_hash": "0xbf41fa3a08446f5a8041fa7a3c80b3e2437a5f102de6d537e1cd9dc9b9258a87",
                "amount": "100000",
                "created_at": "2023-08-07T04:28:37.996150Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Pending",
                "brine_deposit_status": "Pending",
                "deposit_blockchain_hash": "0x3e21ef7e8cd5cb3ebab7fe755d732f17ebc6f2ae5c8a9e1cae2b71ffb162a0aa",
                "amount": "100",
                "created_at": "2023-08-07T04:27:12.461843Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Failed",
                "brine_deposit_status": "Pending",
                "deposit_blockchain_hash": "0xde7bdb6b221f09c066682da04c413eab89f71c08a4f629efee4c1e38eb2fca54",
                "amount": "100",
                "created_at": "2023-08-07T04:26:33.142663Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x0531e0192df925f5d3d9de3333c699a01228ee8e636e5900ea03546ea4f8a35e",
                "amount": "100",
                "created_at": "2023-08-07T04:24:50.528657Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x6789e1aa8db08a697e88381788503ea8e5714a3d59d524a84f619585cb56ace5",
                "amount": "100000",
                "created_at": "2023-08-07T04:16:37.757650Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x24e2dd84b19410a59a00440794f6a70e111ec4fa4a30e3827fdc5e4a000c5461",
                "amount": "100000",
                "created_at": "2023-08-04T16:30:51.278421Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x1b83e88ef5a8f4ad8c2de83ea366474727c7e64b10f6b2d1e1f0a9911170af47",
                "amount": "1000",
                "created_at": "2023-08-04T16:29:01.481086Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0xa4f05745ac8653b1a94f52835a94800c72475f348052dd1584c3b71e6c4d12c1",
                "amount": "1000",
                "created_at": "2023-08-04T13:39:42.430514Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x1e654643b696f33d54a05c2c5f17a104be8a0a17da2bcb7dc310459e0e7c3a52",
                "amount": "1000",
                "created_at": "2023-08-04T06:57"
            }
        ]
    }
}

validate_withdrawal_response= {
    "status": "success",
    "message": "successfully initiated withdrawal",
    "payload": {
        "id": 7819,
        "amount": "0.0000100000000000",
        "token_id": "eth",
        "created_at": "2023-08-07T05:12:50.012516Z",
        "transaction_status": "INITIATED",
        "extras": {
            "errors": [],
            "exp_timestamp": 3997985,
            "quantised_amount": 100000
        }
    }
}

list_withdrawals_response= {
    "status": "success",
    "message": "",
    "payload": {
        "count": 315,
        "next": "",
        "previous": None,
        "results": [
            {
                "id": 7817,
                "amount": "20.0000000000000000",
                "token_id": "usdc",
                "created_at": "2023-08-04T12:34:14.863865Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 20000000
                }
            },
            {
                "id": 7816,
                "amount": "20.0000000000000000",
                "token_id": "usdc",
                "created_at": "2023-08-04T11:11:06.828763Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 20000000
                }
            },
            {
                "id": 7815,
                "amount": "20.0000000000000000",
                "token_id": "usdc",
                "created_at": "2023-08-04T11:10:35.030033Z",
                "transaction_status": "FAILED",
                "extras": {
                    "errors": ["NOT_VALIDATED"],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 20000000
                }
            },
            {
                "id": 7814,
                "amount": "20.0000000000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:42:12.537837Z",
                "transaction_status": "FAILED",
                "extras": {
                    "errors": ["NOT_VALIDATED"],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 200000000000
                }
            },
            {
                "id": 7813,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:30:30.232291Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7812,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:28:54.938646Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7811,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:27:48.480858Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7810,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:26:03.211778Z",
                "transaction_status": "FAILED",
                "extras": {
                    "errors": ["HASH_MISMATCH"],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7809,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:24:56.251147Z",
                "transaction_status": "FAILED",
                "extras": {
                    "errors": ["HASH_MISMATCH"],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7808,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T09:42:35.114010Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            }
        ]
    }
}
