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
    environment=ToltApiEnvironment.DEFAULT,
)

client.embed.create_token(
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

**request:** `CreateTokenEmbedRequest` 
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists partner groups. Filter by program or by the default group, and page with cursors.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListGroupsRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListGroupsRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the group's name, description or public key, ignoring case.
    
</dd>
</dl>

<dl>
<dd>

**default:** `typing.Optional[ListGroupsRequestDefault]` — true lists only default groups, where new partners are placed unless another group is chosen; false lists the others.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a partner group by ID, with the program it belongs to and whether it is the program's default group.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.groups.get(
    id="grp_zUQ8Pt281MsbNDApmDPN3Y2a",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists flows. Filter by program, group, campaign, event or active state, and page with cursors.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFlowsRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListFlowsRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` — Only flows that run for this partner group, by the group id (grp_...) as returned when listing groups.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Only flows that belong to this campaign, by its id as returned when listing campaigns.
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[str]` — Only flows triggered by this event, such as transaction_created or lead_created.
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[ListFlowsRequestActive]` — true lists only active flows, false only paused flows, which do not run.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the flow's name or description, ignoring case.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a flow by ID, with the event it runs on, its conditions and its action: a commission to generate or a group to move the partner to.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.flows.get(
    id="flw_fAyK6FQ6EZngabgw8JifzQgN",
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListClicksRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListClicksRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Limit to one partner, by its id (part_...) as returned when listing partners.
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `typing.Optional[str]` — Limit to one referral link, by its id (lnk_...) as returned when listing links.
    
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
    environment=ToltApiEnvironment.DEFAULT,
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a recorded click by ID, with the partner, link, page, referrer, country, device and browser it came from.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.clicks.get(
    id="clk_mEsbFYv6ZjqXjAoFwokjS6v6",
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.partners.bulk_approve(
    ids=[
        "part_NLYzgNKuSuASvrvoxNtau6SY",
        "part_9fQ2xLLmN3kP8dRvT1wYbHcS"
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

**ids:** `typing.List[str]` — Ids of the partners to act on, as returned when listing partners. Each one succeeds or fails on its own and gets its own entry in results.
    
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.partners.bulk_reject(
    ids=[
        "part_NLYzgNKuSuASvrvoxNtau6SY",
        "part_9fQ2xLLmN3kP8dRvT1wYbHcS"
    ],
    rejection_note="Site does not match our audience.",
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

**ids:** `typing.List[str]` — Ids of the partners to act on, as returned when listing partners. Each one succeeds or fails on its own and gets its own entry in results.
    
</dd>
</dl>

<dl>
<dd>

**rejection_note:** `typing.Optional[str]` — Reason for the rejection, shown to the partner in the partner portal. Null clears an earlier note.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists onboarded partners. Filter by status, program or group, search by name, email or company, and page with cursors.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListPartnersRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListPartnersRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListPartnersRequestStatus]` — Keep only partners at this review stage; approved partners appear as active.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` — Limit to partners in one group, by the group id (grp_...) as returned when listing groups.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the partner's id, email, first name, last name or company name, ignoring case.
    
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
from tolt.partners import CreatePartnersRequestLink

client = ToltApi(
    token="<token>",
    environment=ToltApiEnvironment.DEFAULT,
)

client.partners.create(
    email="sam@example.com",
    program_id="prg_T6z8aRW3XCmvFWP972RKxpAd",
    first_name="Sam",
    last_name="Taylor",
    group_id="grp_zUQ8Pt281MsbNDApmDPN3Y2a",
    link=CreatePartnersRequestLink(
        value="sam",
        param="ref",
    ),
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

**email:** `str` — Partner's email address, where program emails such as the welcome email go. It identifies the partner in the program, so it cannot match another partner's email there, ignoring case.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `str` — Id of the program to add the partner to (prg_...), as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — Partner's first name. With last_name it is used for the default link value when link is omitted.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Partner's last name. With first_name it makes up the name shown for the partner unless display_name is set.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Overrides the name shown for the partner; defaults to the first and last name.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — Business the partner promotes through, if they are a company rather than a person. Leave it out for an individual.
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[str]` — Two-letter ISO country code.
    
</dd>
</dl>

<dl>
<dd>

**website_url:** `typing.Optional[str]` — URL of the partner's website, starting with http:// or https://.
    
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

**status:** `typing.Optional[CreatePartnersRequestStatus]` — Use pending to add the partner as an application that still needs approval instead of an active partner.
    
</dd>
</dl>

<dl>
<dd>

**link:** `typing.Optional[CreatePartnersRequestLink]` — The referral link created with the partner. Leave it out to build the slug from the partner's name, or from the part of the email before the @ when there is no name.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a partner by ID, with their profile, status, group and program.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.partners.get(
    id="part_NLYzgNKuSuASvrvoxNtau6SY",
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.partners.update(
    id="part_NLYzgNKuSuASvrvoxNtau6SY",
    first_name="Sam",
    last_name="Taylor",
    group_id="grp_zUQ8Pt281MsbNDApmDPN3Y2a",
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

**first_name:** `typing.Optional[str]` — Partner's first name, part of the name shown for them unless they have a display name; null clears it.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Partner's family name, shown with first_name in the dashboard and partner portal; null clears it.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — Business the partner promotes through; null clears it.
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[str]` — Partner's country as a two-letter ISO code. Commission flows can match on it.
    
</dd>
</dl>

<dl>
<dd>

**website_url:** `typing.Optional[str]` — URL of the partner's website, starting with http:// or https://; null clears it.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` — Id of a group in the partner's program to move them to (grp_...), as returned when listing groups. Commission flows scoped to that group then apply to them; null removes them from their group.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Makes the partner active. A partner who was not already active is sent the program's approval email.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.partners.approve(
    id="part_NLYzgNKuSuASvrvoxNtau6SY",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rejects the partner. A partner who was not already rejected is sent the program's rejection email with the note.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.partners.reject(
    id="part_NLYzgNKuSuASvrvoxNtau6SY",
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

**rejection_note:** `typing.Optional[str]` — Reason for the rejection, shown to the partner in the partner portal. Null clears an earlier note.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Suspends the partner, with an optional suspension_reason. Use the approve action to make them active again.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.partners.suspend(
    id="part_NLYzgNKuSuASvrvoxNtau6SY",
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

**suspension_reason:** `typing.Optional[str]` — Reason for the suspension, shown to the partner in the partner portal. Null clears an earlier reason.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the programs in your organization, with search, date filters and cursor pagination.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListProgramsRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListProgramsRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the program name, ignoring case.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a program by ID, with its name, currency, website, cookie duration and payout terms.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.programs.get(
    id="prg_T6z8aRW3XCmvFWP972RKxpAd",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists customers. Filter by program, partner, link, click, status or your own customer_id, and page with cursors.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListCustomersRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListCustomersRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Limit to one partner, by its id (part_...) as returned when listing partners.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Exact match on the customer's customer_id field, the id the customer has in your own system or billing provider; not the Tolt customer id.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListCustomersRequestStatus]` — Keep only customers at this lifecycle stage, from signed-up leads through trials to paying, canceled or suspended customers. Leave it out to include every stage.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the customer's email, name, identifier or customer_id, ignoring case.
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` — Only the customers attributed to this click, by its id (clk_...).
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `typing.Optional[str]` — Only customers attributed to this referral link (lnk_...), directly or through one of its clicks.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a customer attributed to a partner. Pass partner_id or link_id, and optionally the click_id that brought them in.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.customers.create(
    email="alex@example.com",
    name="Alex Morgan",
    customer_id="user_4821",
    link_id="lnk_mtTeeckFa1vMdvDFXretQNs6",
    partner_id="part_NLYzgNKuSuASvrvoxNtau6SY",
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

**email:** `typing.Optional[str]` — Customer's email, stored lowercased and used as their identifier. It must not belong to another customer. Provide this or customer_id.
    
</dd>
</dl>

<dl>
<dd>

**promotion_code:** `typing.Optional[str]` — Resolve a code in the partner’s program, ignoring case, preferring partner, group, then program scope. An unmatched code leaves attribution unchanged.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — When the customer was created, for backdating. Defaults to now; lead_at, and active_at for active customers, default to it.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Customer's full name as you want it shown in the dashboard; it does not affect attribution or matching.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Customer's id in your billing system, such as a Stripe customer id. The billing integration matches payments to this customer by it. Provide this or email.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreateCustomersRequestStatus]` — Lifecycle stage of the customer. Defaults to lead (signed up, not paying yet); recording a transaction for the customer makes them active.
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` — Customer's subscription id in your billing system, such as a Stripe subscription id.
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` — Id of the tracked click the customer came from, as returned when listing clicks. It must belong to the partner, and its link is used when link_id is omitted.
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `typing.Optional[str]` — Id of the referral link the customer came through (lnk_...). Without partner_id the link's partner is used; with it, the link must belong to that partner.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Id of the partner who referred the customer (part_...), as returned when listing partners. The customer joins that partner's program. Provide this or link_id.
    
</dd>
</dl>

<dl>
<dd>

**lead_at:** `typing.Optional[datetime.datetime]` — When the customer signed up as a lead, as a timestamp with a time zone, for example 2026-03-01T12:00:00Z. Defaults to created_at.
    
</dd>
</dl>

<dl>
<dd>

**active_at:** `typing.Optional[datetime.datetime]` — When the customer became a paying customer, as a timestamp with a time zone. Defaults to created_at when status is active, otherwise it is set when a transaction is recorded for the customer.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a customer by ID, with its status, the partner it is attributed to and your own customer and subscription IDs.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.customers.get(
    id="cus_LBfjvtfct9pVUeLojMHiGnXv",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a customer's name, email, status, your own IDs, or the click and link the customer came from.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.customers.update(
    id="cus_LBfjvtfct9pVUeLojMHiGnXv",
    name="Alex Morgan",
    status="active",
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

**email:** `typing.Optional[str]` — New email, stored lowercased and used as the customer's identifier. It must not belong to another customer.
    
</dd>
</dl>

<dl>
<dd>

**promotion_code:** `typing.Optional[str]` — Resolve a code in the partner’s program, ignoring case, preferring partner, group, then program scope. An unmatched code leaves attribution unchanged. Null clears the promotion code and its derived attribution.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — When the customer was created, as a timestamp with a time zone, for example 2026-03-01T12:00:00Z. Reports and filters that date customers by creation use it; those that date them by conversion read active_at, which this does not change.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Customer's full name as you want it shown in the dashboard; it does not affect attribution or matching.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateCustomersRequestStatus]` — Lifecycle stage of the customer. Changing it does not set active_at or run commission flows.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Customer's id in your billing system, such as a Stripe customer id. The billing integration matches payments to this customer by it.
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` — Customer's subscription id in your billing system, such as a Stripe subscription id.
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` — Id of the tracked click the customer came from, as returned when listing clicks. It must belong to the customer's partner; link_id is not changed.
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `typing.Optional[str]` — Id of the referral link the customer came through (lnk_...). It must belong to the customer's partner; a customer without a partner takes the link's partner and program.
    
</dd>
</dl>

<dl>
<dd>

**lead_at:** `typing.Optional[datetime.datetime]` — When the customer signed up as a lead, as a timestamp with a time zone, for example 2026-03-01T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**active_at:** `typing.Optional[datetime.datetime]` — When the customer became a paying customer, as a timestamp with a time zone.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a customer. Fails when any of the customer's commissions is paid or already included in a payout.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.customers.delete(
    id="cus_LBfjvtfct9pVUeLojMHiGnXv",
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.commissions.bulk_approve(
    ids=[
        "comm_X85RLnefjTCNrypH4MA1PdSp",
        "comm_3RtV9kQ2mW8nX5pL1sB7cD4f"
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

**ids:** `typing.List[str]` — Ids of the commissions to act on, as returned when listing commissions. Each one succeeds or fails on its own and gets its own entry in results.
    
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.commissions.bulk_decline(
    ids=[
        "comm_X85RLnefjTCNrypH4MA1PdSp",
        "comm_3RtV9kQ2mW8nX5pL1sB7cD4f"
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

**ids:** `typing.List[str]` — Ids of the commissions to act on, as returned when listing commissions. Each one succeeds or fails on its own and gets its own entry in results.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists commissions. Filter by program, partner, customer, transaction, status or type, and page with cursors.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListCommissionsRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListCommissionsRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Limit to one partner, by its id (part_...) as returned when listing partners.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Only commissions for this customer, by Tolt customer id (cus_...) as returned when listing customers.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` — Only commissions linked to this transaction, by its id (txn_...).
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Only commissions in this status, matched exactly, such as pending, approved or paid.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Only commissions whose type equals this stored value exactly.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the commission id or its charge_id, ignoring case.
    
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
    environment=ToltApiEnvironment.DEFAULT,
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a commission by ID, with its amount, status, type and partner, plus its customer and transaction when it has them.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.commissions.get(
    id="comm_X85RLnefjTCNrypH4MA1PdSp",
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.commissions.update(
    id="comm_X85RLnefjTCNrypH4MA1PdSp",
    amount=1000,
    revenue=5000,
    status="approved",
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

**amount:** `typing.Optional[int]` — What the partner earns for this commission, in minor units of the program currency (cents for USD).
    
</dd>
</dl>

<dl>
<dd>

**revenue:** `typing.Optional[int]` — The sale amount the commission is based on, in minor units of the program currency.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateCommissionsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — Free-form label for where the commission came from, such as stripe or api.
    
</dd>
</dl>

<dl>
<dd>

**charge_id:** `typing.Optional[str]` — Id of the payment in your billing system that the commission is for, such as a Stripe charge id.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` — Id of the transaction the commission is for (txn_...). It must belong to the commission's customer, or to its partner and program, and must not be refunded.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — When the commission was earned, as a timestamp with a time zone, for example 2026-03-01T12:00:00Z. Reports and filters by creation date place the commission on this date; the upcoming approvals forecast goes by its scheduled approval date, which this does not change.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a commission. Fails for paid commissions, refund commissions, commissions on a refunded transaction, and those on a confirmed or legacy autopayout invoice.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.commissions.delete(
    id="comm_X85RLnefjTCNrypH4MA1PdSp",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks a commission approved so it is included in the next payout. Fails for paid commissions, refund commissions, commissions on a refunded transaction, and those on a confirmed or legacy autopayout invoice.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.commissions.approve(
    id="comm_X85RLnefjTCNrypH4MA1PdSp",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks a commission declined so it is left out of payouts until it is approved again. Fails for paid commissions, refund commissions, commissions on a refunded transaction, and those on a confirmed or legacy autopayout invoice.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.commissions.decline(
    id="comm_X85RLnefjTCNrypH4MA1PdSp",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists transactions. Filter by program, partner, customer or status, and page with cursors.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTransactionsRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListTransactionsRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Limit to one partner, by its id (part_...) as returned when listing partners.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Only transactions from this customer, by Tolt customer id (cus_...) as returned when listing customers.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Only transactions in this status, matched exactly, such as paid or refunded.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the transaction id or its charge_id, ignoring case.
    
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.transactions.create(
    product_id="prod_pro",
    product_name="Pro plan",
    amount=5000,
    customer_id="cus_LBfjvtfct9pVUeLojMHiGnXv",
    billing_type="subscription",
    interval="month",
    source="api",
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

**amount:** `int` — The payment amount in the smallest unit of the program currency (cents for USD); percentage commissions are calculated from it.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — Id of the customer who paid (cus_...), as returned when listing customers. The transaction goes to that customer's partner and program, and the customer becomes active.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — When the payment happened, as a timestamp with a time zone, for example 2026-03-01T12:00:00Z. Reports and date filters place the transaction on this date. Defaults to now.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `typing.Optional[str]` — Id of the purchased product in your billing system. Commission flows can match on it.
    
</dd>
</dl>

<dl>
<dd>

**product_name:** `typing.Optional[str]` — Readable name of the purchased product, such as Pro plan. It is saved as the transaction's product name, which revenue_by_product groups revenue by; flows match on product_id, not on this name.
    
</dd>
</dl>

<dl>
<dd>

**billing_type:** `typing.Optional[str]` — Kind of payment: subscription for a recurring payment, or one_time. Commission flows can match on it.
    
</dd>
</dl>

<dl>
<dd>

**charge_id:** `typing.Optional[str]` — Id of the payment in your billing system, such as a Stripe charge id. A customer can have only one transaction per charge_id, so retrying a create with the same value returns 409 instead of booking the payment twice. An empty or whitespace-only charge_id is stored as no charge id and is not checked; any other value is stored and compared exactly as sent.
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` — Id of the tracked click behind this payment, as returned when listing clicks. Commission flows use its link before falling back to the customer's link.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[str]` — Billing period of a subscription payment: month or year. Commission flows can match on it. Flows can also split a yearly payment into monthly commissions.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — Where the transaction came from, such as stripe or api. Commissions that flows create from it copy this value.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a transaction by ID, with its amount, status, billing details, products and the customer it belongs to.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.transactions.get(
    id="txn_fB3egT1sKNVNu3ZYuU1ypYDA",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a transaction's amount, status, billing or product details. Refunded transactions cannot be modified.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.transactions.update(
    id="txn_fB3egT1sKNVNu3ZYuU1ypYDA",
    amount=5000,
    product_name="Pro plan",
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

**amount:** `typing.Optional[int]` — The payment amount in the smallest unit of the program currency (cents for USD); percentage commissions are calculated from it.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Payment status text, such as paid, which is what new transactions get. refunded is not accepted here: refund a transaction with the refund action. null clears the status.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — Where the transaction came from, such as stripe or api.
    
</dd>
</dl>

<dl>
<dd>

**billing_type:** `typing.Optional[str]` — Kind of payment: subscription for a recurring payment, or one_time.
    
</dd>
</dl>

<dl>
<dd>

**charge_id:** `typing.Optional[str]` — Id of the payment in your billing system, such as a Stripe charge id.
    
</dd>
</dl>

<dl>
<dd>

**click_id:** `typing.Optional[str]` — Id of the tracked click behind this payment, as returned when listing clicks.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `typing.Optional[str]` — Id of the purchased product in your billing system.
    
</dd>
</dl>

<dl>
<dd>

**product_name:** `typing.Optional[str]` — Readable name of the purchased product, such as Pro plan. It is saved as the transaction's product name, which revenue_by_product groups revenue by; flows match on product_id, not on this name. null clears it.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[str]` — Billing period of a subscription payment: month or year.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — When the payment happened, as a timestamp with a time zone, for example 2026-03-01T12:00:00Z. Reports and date filters place the transaction on this date.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a transaction. Refunded transactions and transactions that already have commissions cannot be deleted.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.transactions.delete(
    id="txn_fB3egT1sKNVNu3ZYuU1ypYDA",
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.transactions.refund(
    id="txn_fB3egT1sKNVNu3ZYuU1ypYDA",
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.transactions.rerun_flows(
    id="txn_fB3egT1sKNVNu3ZYuU1ypYDA",
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListLinksRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListLinksRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Limit to one partner, by its id (part_...) as returned when listing partners.
    
</dd>
</dl>

<dl>
<dd>

**param:** `typing.Optional[str]` — Only links using this URL parameter name exactly, such as `ref` in `?ref=sam`.
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Only links with this exact slug, such as `sam` in `?ref=sam`.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the link's slug (value) or parameter name, ignoring case.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a referral link for a partner. The value must be unique for its parameter, and param defaults to the program's.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.links.create(
    value="sam",
    param="ref",
    partner_id="part_NLYzgNKuSuASvrvoxNtau6SY",
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

**value:** `str` — Slug that identifies the partner in referral URLs, such as `sam` in `?ref=sam`, saved in lowercase. Pick one that no other link uses with the same parameter; a taken slug returns an error.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `str` — Id of the partner who owns the link (part_...), as returned when listing partners. The link is created in that partner's program.
    
</dd>
</dl>

<dl>
<dd>

**param:** `typing.Optional[str]` — Query parameter of the link, e.g. `ref` in `?ref=sam`. Leave it out or send an empty string to use the program's first link parameter, which is what gets stored.
    
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
    environment=ToltApiEnvironment.DEFAULT,
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.links.get(
    id="lnk_mtTeeckFa1vMdvDFXretQNs6",
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.links.update(
    id="lnk_mtTeeckFa1vMdvDFXretQNs6",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**param:** `typing.Optional[str]` — New query parameter of the link, e.g. `ref` in `?ref=sam`. URLs with the old parameter stop matching this link.
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — New slug, e.g. `sam` in `?ref=sam`, stored lowercased. URLs using the old slug stop matching this link.
    
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.links.delete(
    id="lnk_mtTeeckFa1vMdvDFXretQNs6",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists promotion codes. Filter by program, partner or type, and page with cursors.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListPromotionCodesRequestOrder]` — Ranking direction: desc puts the most recently created or updated rows first.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListPromotionCodesRequestSort]` — Timestamp to order and page by: created_at follows creation order, updated_at follows each item's most recent change.
    
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

**created_after:** `typing.Optional[datetime.datetime]` — Start of a window on when items were created: items created at this time or later are included, for example 2026-01-01T00:00:00Z. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — End of a window on when items were created: only items created before this time are included. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only items last changed at or after this moment; with sort=updated_at, use it to fetch what changed since a previous sync.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Only items last changed before this moment; pair it with updated_after to fetch what changed in a period.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Limit to one partner, by its id (part_...) as returned when listing partners.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListPromotionCodesRequestType]` — Only codes giving this kind of discount: a fixed amount off or a percentage off.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text matched anywhere in the code, ignoring case.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a promotion code for a partner, so customers who use it are credited to them. A partner cannot have the same code twice.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.promotion_codes.create(
    code="SAM20",
    type="percentage",
    value="20",
    partner_id="part_NLYzgNKuSuASvrvoxNtau6SY",
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

**code:** `str` — The discount code as customers enter it at checkout. Customers and payments that use it are attributed to the code's partner. A partner cannot have the same code twice, ignoring case. Recording it here does not create it in your billing system.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `str` — Id of the partner the code belongs to (part_...), as returned when listing partners. The code is created in that partner's program.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreatePromotionCodesRequestType]` — Whether value is a percent off or a fixed amount off.
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Size of the discount as a plain decimal: a percent from 0 to 100 for percentage codes ("20" is 20%), or an amount from 0 to 1,000,000 in major units of the program currency for fixed codes ("20" is 20.00).
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a promotion code by ID, with its discount type and value and the partner, group or program it belongs to.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.promotion_codes.get(
    id="promo_gTCAUsWfdmN2GuCVRaHWNRan",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a promotion code's code, discount type or value.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.promotion_codes.update(
    id="promo_gTCAUsWfdmN2GuCVRaHWNRan",
    code="SAM20",
    type="percentage",
    value="20",
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

**code:** `typing.Optional[str]` — The discount code as customers enter it at checkout. Customers and payments that use it are attributed to the code's partner. A partner cannot have the same code twice, ignoring case.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdatePromotionCodesRequestType]` — Whether value is a percent off or a fixed amount off.
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Size of the discount as a plain decimal: a percent from 0 to 100 for percentage codes ("20" is 20%), or an amount from 0 to 1,000,000 in major units of the program currency for fixed codes ("20" is 20.00). null clears it.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a promotion code, so customers who use it afterwards are no longer attributed through it.
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
    environment=ToltApiEnvironment.DEFAULT,
)

client.promotion_codes.delete(
    id="promo_gTCAUsWfdmN2GuCVRaHWNRan",
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns revenue, commission, customer and partner totals for the organization or one program over a date range.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Earliest day to include, by creation date. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — Latest day to include, by creation date; the whole day counts. Leave it out for no upper bound.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one row of revenue, commissions, customers and clicks per partner over a date range, sorted and paged by offset.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Earliest day to include, by creation date (customers by the day they became active). Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — Latest day to include, by creation date (customers by the day they became active); the whole day counts. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Only include transactions and commissions in this currency, such as USD; matching ignores case. Rows without their own currency use their program's.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — How many rows to skip before this page begins.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PartnersReportsRequestSort]` — Metric to rank by, computed over the date window.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PartnersReportsRequestOrder]` — Ranking direction: desc puts the highest values first.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one row of revenue, commissions, customers and clicks per link over a date range, sorted and paged by offset.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Earliest day to include, by creation date (customers by the day they became active). Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — Latest day to include, by creation date (customers by the day they became active); the whole day counts. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Only include transactions and commissions in this currency, such as USD; matching ignores case. Rows without their own currency use their program's.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — How many rows to return in one page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — How many rows to skip before this page begins.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[LinksReportsRequestSort]` — Metric to rank by, computed over the date window.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[LinksReportsRequestOrder]` — Ranking direction: desc puts the highest values first.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns revenue, commissions, customers and clicks per day, week or month over a date range, ready to chart.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Earliest day to include, by creation date (customers by the day they became active). Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — Latest day to include, by creation date (customers by the day they became active); the whole day counts. Leave it out for no upper bound.
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `typing.Optional[TimeseriesReportsRequestGranularity]` — Bucket size of the series; weeks start on Monday, months on the 1st, and each bucket is labeled with its first day.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Only include transactions and commissions in this currency, such as USD; matching ignores case. Rows without their own currency use their program's.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns how many customers are in each subscription status for the organization or one program.
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
    environment=ToltApiEnvironment.DEFAULT,
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

**program_id:** `typing.Optional[str]` — Limit to one program, by its id (prg_...) as returned when listing programs.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Earliest day to include, by the day customers became active. Leave it out for no lower bound.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — Latest day to include, by the day customers became active; the whole day counts. Leave it out for no upper bound.
    
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

