# GlutaNex website (glutanex.co.in)

Static store built by `python3 _build/build.py` (writes the pages into the repository root), with Vercel
serverless functions in `api/`. Prices live in `api/_shared.js` and `_build/build.py` and must match.

## How orders flow

| Payment | What happens |
|---|---|
| **Pay online** (Razorpay, full amount) | `api/create-order` prices the cart on the server and opens Razorpay. `api/verify` checks the signature, confirms with Razorpay that the payment is captured for the server price, marks a reward code as used, and sends the order to the **Order Desk** as PAID. Not booked with Delhivery here. |
| **Cash on Delivery** (nothing paid upfront) | `api/cod-order` prices the cart (reward code included) on the server, checks Delhivery COD availability for the pincode (409 if not available), books the **Delhivery** shipment (COD amount = order total) and always saves the order in the **Order Desk** (with the AWB; if booking failed, with a warning to book it by hand). The reward code is marked used once the order is placed. Rate-limited per mobile number and for the whole shop. |
| **WhatsApp** | Opens WhatsApp with the order text (also the fallback if neither Delhivery nor the Order Desk is set up). |

Order numbers are `GX` + 8 digits. Order Desk brand id: `gx` (Night Cream = Order Desk product `gx1`).
Shiprocket is no longer used for orders; `api/_shiprocket.js` only tracks parcels booked before the switch
(and answers pincode lookups while Delhivery is not set up), and only if its old env vars are still set.

`cod-order` and `delhivery-check` run inside `api/hub.js` (see the rewrite in `vercel.json`) to stay within the
Vercel Hobby limit of 12 functions.

## Environment variables (Vercel project settings)

| Name | Value |
|---|---|
| `WEB_ORDER_KEY` | Same secret key as the Order Desk project |
| `ORDERDESK_URL` | Optional, default `https://www.skinday.shop` |
| `DELHIVERY_TOKEN` | Delhivery API token |
| `DELHIVERY_PICKUP` | `mohammed nihal\|Beauty Mart` (pickup names as registered in Delhivery; the first one is the one Delhivery accepts) |
| `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET` | Razorpay keys (already set) |
| `KV_REST_API_URL`, `KV_REST_API_TOKEN` | Upstash Redis (already set): reward codes, rate limits, COD order tracking |
| Optional | `DELHIVERY_ENV=staging`, `DELHIVERY_MODE=Express` |

Check Delhivery after deploying: open `/api/delhivery-check` (books nothing, shows no secrets).
