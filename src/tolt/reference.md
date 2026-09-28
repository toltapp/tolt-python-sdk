# Reference
## Embed
<details><summary><code>client.embed.<a href="src/tolt/embed/client.py">create_embed_token</a>(...) -> CreateEmbedTokenResponse</code></summary>
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

client.embed.create_embed_token()

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

**partner:** `typing.Optional[CreateEmbedTokenRequestPartner]` 
    
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
<details><summary><code>client.groups.<a href="src/tolt/groups/client.py">list_groups</a>(...) -> ListGroupsResponse</code></summary>
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

client.groups.list_groups()

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

<details><summary><code>client.groups.<a href="src/tolt/groups/client.py">get_group</a>(...) -> GetGroupResponse</code></summary>
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

client.groups.get_group(
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
<details><summary><code>client.flows.<a href="src/tolt/flows/client.py">list_flows</a>(...) -> ListFlowsResponse</code></summary>
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

client.flows.list_flows()

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

<details><summary><code>client.flows.<a href="src/tolt/flows/client.py">get_flow</a>(...) -> GetFlowResponse</code></summary>
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

client.flows.get_flow(
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
<details><summary><code>client.clicks.<a href="src/tolt/clicks/client.py">create_click</a>(...) -> CreateClickResponse</code></summary>
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

client.clicks.create_click(
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

**request:** `CreateClickRequest` 
    
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

<details><summary><code>client.clicks.<a href="src/tolt/clicks/client.py">get_click</a>(...) -> GetClickResponse</code></summary>
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

client.clicks.get_click(
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
<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">bulk_approve_partners</a>(...) -> BulkApprovePartnersResponse</code></summary>
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

client.partners.bulk_approve_partners(
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

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">bulk_reject_partners</a>(...) -> BulkRejectPartnersResponse</code></summary>
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

client.partners.bulk_reject_partners(
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

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">list_partners</a>(...) -> ListPartnersResponse</code></summary>
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

client.partners.list_partners()

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

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">create_partner</a>(...) -> CreatePartnerResponse</code></summary>
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

client.partners.create_partner(
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

**group_id:** `typing.Optional[str]` — Group in the program. Defaults to the program's default group.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreatePartnerRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**link:** `typing.Optional[CreatePartnerRequestLink]` — The referral link created with the partner. Defaults to a slug of the name or email.
    
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

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">get_partner</a>(...) -> GetPartnerResponse</code></summary>
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

client.partners.get_partner(
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

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">update_partner</a>(...) -> UpdatePartnerResponse</code></summary>
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

client.partners.update_partner(
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

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">approve_partner</a>(...) -> ApprovePartnerResponse</code></summary>
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

client.partners.approve_partner(
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

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">reject_partner</a>(...) -> RejectPartnerResponse</code></summary>
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

client.partners.reject_partner(
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

<details><summary><code>client.partners.<a href="src/tolt/partners/client.py">suspend_partner</a>(...) -> SuspendPartnerResponse</code></summary>
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

client.partners.suspend_partner(
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
<details><summary><code>client.programs.<a href="src/tolt/programs/client.py">list_programs</a>(...) -> ListProgramsResponse</code></summary>
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

client.programs.list_programs()

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

<details><summary><code>client.programs.<a href="src/tolt/programs/client.py">get_program</a>(...) -> GetProgramResponse</code></summary>
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

client.programs.get_program(
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
<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">list_customers</a>(...) -> ListCustomersResponse</code></summary>
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

client.customers.list_customers()

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

<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">create_customer</a>(...) -> CreateCustomerResponse</code></summary>
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

client.customers.create_customer()

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

**status:** `typing.Optional[str]` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">get_customer</a>(...) -> GetCustomerResponse</code></summary>
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

client.customers.get_customer(
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

<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">update_customer</a>(...) -> UpdateCustomerResponse</code></summary>
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

client.customers.update_customer(
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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
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

<details><summary><code>client.customers.<a href="src/tolt/customers/client.py">delete_customer</a>(...) -> DeleteCustomerResponse</code></summary>
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

client.customers.delete_customer(
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
<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">bulk_approve_commissions</a>(...) -> BulkApproveCommissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approves up to 100 commissions. Each id is processed on its own and the response reports the outcome per id, with the error code for any that were refused.
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

client.commissions.bulk_approve_commissions(
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

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">bulk_decline_commissions</a>(...) -> BulkDeclineCommissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Declines up to 100 commissions. Each id is processed on its own and the response reports the outcome per id, with the error code for any that were refused.
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

client.commissions.bulk_decline_commissions(
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

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">list_commissions</a>(...) -> ListCommissionsResponse</code></summary>
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

client.commissions.list_commissions()

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

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">create_commission</a>(...) -> CreateCommissionResponse</code></summary>
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

client.commissions.create_commission(
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

**request:** `CreateCommissionRequest` 
    
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

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">get_commission</a>(...) -> GetCommissionResponse</code></summary>
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

client.commissions.get_commission(
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

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">update_commission</a>(...) -> UpdateCommissionResponse</code></summary>
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

client.commissions.update_commission(
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

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">delete_commission</a>(...) -> DeleteCommissionResponse</code></summary>
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

client.commissions.delete_commission(
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

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">approve_commission</a>(...) -> ApproveCommissionResponse</code></summary>
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

client.commissions.approve_commission(
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

<details><summary><code>client.commissions.<a href="src/tolt/commissions/client.py">decline_commission</a>(...) -> DeclineCommissionResponse</code></summary>
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

client.commissions.decline_commission(
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
<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">list_transactions</a>(...) -> ListTransactionsResponse</code></summary>
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

client.transactions.list_transactions()

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

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">create_transaction</a>(...) -> CreateTransactionResponse</code></summary>
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

client.transactions.create_transaction(
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

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">get_transaction</a>(...) -> GetTransactionResponse</code></summary>
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

client.transactions.get_transaction(
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

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">update_transaction</a>(...) -> UpdateTransactionResponse</code></summary>
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

client.transactions.update_transaction(
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

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">delete_transaction</a>(...) -> DeleteTransactionResponse</code></summary>
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

client.transactions.delete_transaction(
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

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">refund_transaction</a>(...) -> RefundTransactionResponse</code></summary>
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

client.transactions.refund_transaction(
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

<details><summary><code>client.transactions.<a href="src/tolt/transactions/client.py">rerun_transaction_flows</a>(...) -> RerunTransactionFlowsResponse</code></summary>
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

client.transactions.rerun_transaction_flows(
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
<details><summary><code>client.links.<a href="src/tolt/links/client.py">list_links</a>(...) -> ListLinksResponse</code></summary>
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

client.links.list_links()

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

<details><summary><code>client.links.<a href="src/tolt/links/client.py">create_link</a>(...) -> CreateLinkResponse</code></summary>
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

client.links.create_link(
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

<details><summary><code>client.links.<a href="src/tolt/links/client.py">get_link</a>(...) -> GetLinkResponse</code></summary>
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

client.links.get_link(
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

<details><summary><code>client.links.<a href="src/tolt/links/client.py">update_link</a>(...) -> UpdateLinkResponse</code></summary>
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

client.links.update_link(
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

<details><summary><code>client.links.<a href="src/tolt/links/client.py">delete_link</a>(...) -> DeleteLinkResponse</code></summary>
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

client.links.delete_link(
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
<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">list_promotion_codes</a>(...) -> ListPromotionCodesResponse</code></summary>
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

client.promotion_codes.list_promotion_codes()

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

<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">create_promotion_code</a>(...) -> CreatePromotionCodeResponse</code></summary>
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

client.promotion_codes.create_promotion_code(
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

**type:** `typing.Optional[str]` 
    
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

<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">get_promotion_code</a>(...) -> GetPromotionCodeResponse</code></summary>
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

client.promotion_codes.get_promotion_code(
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

<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">update_promotion_code</a>(...) -> UpdatePromotionCodeResponse</code></summary>
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

client.promotion_codes.update_promotion_code(
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

**type:** `typing.Optional[str]` 
    
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

<details><summary><code>client.promotion_codes.<a href="src/tolt/promotion_codes/client.py">delete_promotion_code</a>(...) -> DeletePromotionCodeResponse</code></summary>
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

client.promotion_codes.delete_promotion_code(
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
<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">overview</a>(...) -> ReportsOverviewResponse</code></summary>
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

<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">partners</a>(...) -> ReportsPartnersResponse</code></summary>
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

**sort:** `typing.Optional[ReportsPartnersRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ReportsPartnersRequestOrder]` 
    
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

<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">links</a>(...) -> ReportsLinksResponse</code></summary>
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

**sort:** `typing.Optional[ReportsLinksRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ReportsLinksRequestOrder]` 
    
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

<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">timeseries</a>(...) -> ReportsTimeseriesResponse</code></summary>
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

**granularity:** `typing.Optional[ReportsTimeseriesRequestGranularity]` 
    
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

<details><summary><code>client.reports.<a href="src/tolt/reports/client.py">customer_stats</a>(...) -> ReportsCustomerStatsResponse</code></summary>
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

