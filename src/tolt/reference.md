# Reference
## Embed
<details><summary><code>client.embed.<a href="src/tolt/embed/client.py">create_token</a>(...) -> CreateTokenEmbedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mint a short-lived, partner-scoped token for the embedded referral dashboard. Safe to send to the browser.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.embed.create_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner:** `typing.Optional[CreateTokenEmbedRequestPartner]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Groups
<details><summary><code>client.groups.<a href="src/tolt/groups/client.py">list</a>(...) -> ListGroupsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.groups.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListGroupsRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListGroupsRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**default:** `typing.Optional[ListGroupsRequestDefault]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/tolt/groups/client.py">get</a>(...) -> GetGroupsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.groups.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Flows
<details><summary><code>client.flows.<a href="src/tolt/flows/client.py">list</a>(...) -> ListFlowsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.flows.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFlowsRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListFlowsRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[ListFlowsRequestActive]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.<a href="src/tolt/flows/client.py">get</a>(...) -> GetFlowsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.flows.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Clicks
<details><summary><code>client.clicks.<a href="src/tolt/clicks/client.py">list</a>(...) -> ListClicksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists recorded clicks. Filter by program, partner, link, country, or device, and page with cursors.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.clicks.list(
    country="Canada",
    device="desktop",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListClicksRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListClicksRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Filter by the click's stored country, matched exactly (values are not normalized). Clicks recorded by the tracking script store a country name (e.g. `Canada`); clicks created through the API store a 2-letter ISO code (e.g. `CA`). Filter by the exact form you expect.
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[str]` — Device type, e.g. `desktop`, `mobile` or `tablet`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clicks.<a href="src/tolt/clicks/client.py">create</a>(...) -> CreateClicksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Records a click on a partner's link from your own server, for visits the browser script cannot see. Identify the source by link_id, by partner_id with an optional link_id, or by the link's param and value; the partner and program are resolved from it. Pass the returned id as click_id when you create the customer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.clicks.create(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateClicksRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clicks.<a href="src/tolt/clicks/client.py">get</a>(...) -> GetClicksResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.clicks.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Partners
<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">bulk_approve</a>(...) -> BulkApprovePartnersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approves up to 100 partners. Each id is processed on its own and the response reports the outcome per id, so one refused partner does not fail the request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.bulk_approve(
    ids=[
        "part_9fQ2xLL",
        "part_3RtV9k"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.List[str]` — Up to 100 ids. Duplicates are processed once.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">bulk_reject</a>(...) -> BulkRejectPartnersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rejects up to 100 partners with an optional shared rejection note. Each id is processed on its own and the response reports the outcome per id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.bulk_reject(
    ids=[
        "part_9fQ2xLL",
        "part_3RtV9k"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.List[str]` — Up to 100 ids. Duplicates are processed once.
    
</dd>
</dl>

<dl>
<dd>

**rejection_note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">list</a>(...) -> ListPartnersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListPartnersRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListPartnersRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListPartnersRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">create</a>(...) -> CreatePartnersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an onboarded partner together with their referral link. The link value defaults to a slug of the partner's name or email and the parameter to the program's first link parameter. Omit group_id to place the partner in the program's default group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.create(
    email="sam@acme.com",
    program_id="prg_YRsbPDAK",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Unique within the program, compared case-insensitively.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Overrides the name shown for the partner; defaults to the first and last name.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[str]` — Two-letter ISO country code.
    
</dd>
</dl>

<dl>
<dd>

**website_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — Backdate the partner's creation time. Defaults to now.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` — Group in the program. Defaults to the program's default group.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreatePartnersRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**link:** `typing.Optional[CreatePartnersRequestLink]` — The referral link created with the partner. Defaults to a slug of the name or email.
    
</dd>
</dl>

<dl>
<dd>

**notify_partner:** `typing.Optional[bool]` — Send the partner the program's welcome email. Only goes out when the program's welcome email is enabled and the partner is active.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">get</a>(...) -> GetPartnersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">update</a>(...) -> UpdatePartnersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edits profile fields and group membership. Status changes go through the approve, reject and suspend actions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**website_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">approve</a>(...) -> ApprovePartnersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.approve(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">reject</a>(...) -> RejectPartnersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.reject(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**rejection_note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">suspend</a>(...) -> SuspendPartnersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.partners.suspend(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**suspension_reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Programs
<details><summary><code>client.programs.<a href="src/tolt/programs/client.py">list</a>(...) -> ListProgramsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.programs.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListProgramsRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListProgramsRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programs.<a href="src/tolt/programs/client.py">get</a>(...) -> GetProgramsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.programs.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers
<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">list</a>(...) -> ListCustomersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.customers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListCustomersRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListCustomersRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListCustomersRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">create</a>(...) -> CreateCustomersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.customers.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**promotion_code:** `typing.Optional[str]` — Resolve a code in the partner’s program, preferring partner, group, then program scope. An unmatched code leaves attribution unchanged.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreateCustomersRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**active_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">get</a>(...) -> GetCustomersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.customers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">update</a>(...) -> UpdateCustomersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.customers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**promotion_code:** `typing.Optional[str]` — Resolve a code in the partner’s program, preferring partner, group, then program scope. An unmatched code leaves attribution unchanged. Null clears the promotion code and its derived attribution.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateCustomersRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**active_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">delete</a>(...) -> DeleteCustomersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.customers.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Commissions
<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">bulk_approve</a>(...) -> BulkApproveCommissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approves up to 100 commissions and reports the outcome per id. Successful changes and affected draft invoice totals commit together.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.bulk_approve(
    ids=[
        "part_9fQ2xLL",
        "part_3RtV9k"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.List[str]` — Up to 100 ids. Duplicates are processed once.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">bulk_decline</a>(...) -> BulkDeclineCommissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Declines up to 100 commissions and reports the outcome per id. Successful changes and affected draft invoice totals commit together.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.bulk_decline(
    ids=[
        "part_9fQ2xLL",
        "part_3RtV9k"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.List[str]` — Up to 100 ids. Duplicates are processed once.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">list</a>(...) -> ListCommissionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListCommissionsRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListCommissionsRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">create</a>(...) -> CreateCommissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Supports historical created_at values. Status defaults to approved when omitted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.create(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateCommissionsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">get</a>(...) -> GetCommissionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">update</a>(...) -> UpdateCommissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unpaid commissions can be changed unless linked to a confirmed invoice or legacy autopayout invoice. Affected draft invoice totals are recalculated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[int]` — Monetary amount as an integer in the smallest currency unit (cents), e.g. 500 = 5.00
    
</dd>
</dl>

<dl>
<dd>

**revenue:** `typing.Optional[int]` — Monetary amount as an integer in the smallest currency unit (cents), e.g. 500 = 5.00
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**charge_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">delete</a>(...) -> DeleteCommissionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">approve</a>(...) -> ApproveCommissionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.approve(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">decline</a>(...) -> DeclineCommissionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.commissions.decline(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transactions
<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">list</a>(...) -> ListTransactionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.transactions.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTransactionsRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListTransactionsRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">create</a>(...) -> CreateTransactionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Supports historical created_at values. product_id and product_name are stored and returned in product_ids and product_names arrays.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.transactions.create(
    amount=1,
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `int` — Monetary amount as an integer in the smallest currency unit (cents), e.g. 500 = 5.00
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**product_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**charge_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">get</a>(...) -> GetTransactionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.transactions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">update</a>(...) -> UpdateTransactionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.transactions.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[int]` — Monetary amount as an integer in the smallest currency unit (cents), e.g. 500 = 5.00
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**charge_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**product_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">delete</a>(...) -> DeleteTransactionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.transactions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">refund</a>(...) -> RefundTransactionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unpaid commissions are zeroed while preserving their original deducted commission amount, and affected draft invoices are recalculated. Paid commissions and commissions linked to legacy autopayout invoices receive a negative reversal.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.transactions.refund(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">rerun_flows</a>(...) -> RerunFlowsTransactionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-queues the transaction for asynchronous flow processing. Only transactions without an existing commission are eligible, so a rerun cannot create a duplicate commission.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.transactions.rerun_flows(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Links
<details><summary><code>client.links.<a href="src/tolt/links/client.py">list</a>(...) -> ListLinksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists ordinary links. Campaign-managed links are excluded.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.links.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListLinksRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListLinksRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**param:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.links.<a href="src/tolt/links/client.py">create</a>(...) -> CreateLinksResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.links.create(
    value="value",
    partner_id="partner_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**value:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**param:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.links.<a href="src/tolt/links/client.py">get_by_param_value</a>(...) -> GetByParamValueLinksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Looks up a single link by its parameter and value (value matched case-insensitively). Returns 404 when none matches.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.links.get_by_param_value(
    param="ref",
    value="sam",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**param:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Matched case-insensitively.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.links.<a href="src/tolt/links/client.py">get</a>(...) -> GetLinksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an ordinary or campaign-managed link by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.links.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.links.<a href="src/tolt/links/client.py">update</a>(...) -> UpdateLinksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an ordinary link. Campaign-managed links must be changed through campaigns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.links.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**param:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.links.<a href="src/tolt/links/client.py">delete</a>(...) -> DeleteLinksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an ordinary link. Campaign-managed links must be changed through campaigns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.links.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PromotionCodes
<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">list</a>(...) -> ListPromotionCodesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.promotion_codes.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListPromotionCodesRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListPromotionCodesRequestSort]` — Column the list is ordered and paged by.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Continue after a position: the next_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with ending_before.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Page backward from a position: the prev_cursor of a previous page, or an item id when sorting by created_at. Cannot be combined with starting_after.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only items created at or after this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only items created before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items updated at or after this ISO 8601 time. Combine with sort=updated_at to sync changes.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items updated before this ISO 8601 time.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListPromotionCodesRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">create</a>(...) -> CreatePromotionCodesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.promotion_codes.create(
    code="code",
    partner_id="partner_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreatePromotionCodesRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">get</a>(...) -> GetPromotionCodesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.promotion_codes.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">update</a>(...) -> UpdatePromotionCodesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.promotion_codes.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdatePromotionCodesRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">delete</a>(...) -> DeletePromotionCodesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.promotion_codes.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reports
<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">overview</a>(...) -> OverviewReportsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.reports.overview()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">partners</a>(...) -> PartnersReportsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.reports.partners()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PartnersReportsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PartnersReportsRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">links</a>(...) -> LinksReportsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.reports.links()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[LinksReportsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[LinksReportsRequestOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">timeseries</a>(...) -> TimeseriesReportsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.reports.timeseries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `typing.Optional[TimeseriesReportsRequestGranularity]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">customer_stats</a>(...) -> CustomerStatsReportsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from tolt import ToltApi
from tolt.environment import ToltApiEnvironment

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.PRODUCTION,
)

client.reports.customer_stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

