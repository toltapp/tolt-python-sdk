# Reference
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

**starting_after:** `typing.Optional[str]` 
    
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

**starting_after:** `typing.Optional[str]` 
    
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
<details><summary><code>client.clicks.<a href="src/tolt/clicks/client.py">list_clicks</a>(...) -> ListClicksResponse</code></summary>
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

client.clicks.list_clicks()

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

**starting_after:** `typing.Optional[str]` 
    
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

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**browser:** `typing.Optional[str]` 
    
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

**starting_after:** `typing.Optional[str]` 
    
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

**starting_after:** `typing.Optional[str]` 
    
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

**starting_after:** `typing.Optional[str]` 
    
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

client.customers.create_customer(
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

**request:** `CreateCustomerRequest` 
    
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

**starting_after:** `typing.Optional[str]` 
    
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

**starting_after:** `typing.Optional[str]` 
    
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
    customer_id="customerId",
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

**starting_after:** `typing.Optional[str]` 
    
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
    partner_id="partnerId",
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

**starting_after:** `typing.Optional[str]` 
    
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
    partner_id="partnerId",
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

