# JSON Comparison Result

## Summary Section
- Total number of value differences: 0
- Total keys only in json_a: 32
- Total keys only in json_b: 0

## Table 1 – Value Differences
No value differences found.

## Table 2 – Key Differences
| Key Path | Exists In |
|---|---|
| connector_config.partner.connection_time_out | json_a |
| mapped_message_field.partner.request[0].response_chain_flag | json_a |
| mapped_message_field.partner.request[10].response_chain_flag | json_a |
| mapped_message_field.partner.request[11].response_chain_flag | json_a |
| mapped_message_field.partner.request[12].response_chain_flag | json_a |
| mapped_message_field.partner.request[13].response_chain_flag | json_a |
| mapped_message_field.partner.request[1].response_chain_flag | json_a |
| mapped_message_field.partner.request[2].response_chain_flag | json_a |
| mapped_message_field.partner.request[3].response_chain_flag | json_a |
| mapped_message_field.partner.request[4].response_chain_flag | json_a |
| mapped_message_field.partner.request[5].response_chain_flag | json_a |
| mapped_message_field.partner.request[6].response_chain_flag | json_a |
| mapped_message_field.partner.request[7].response_chain_flag | json_a |
| mapped_message_field.partner.request[8].response_chain_flag | json_a |
| mapped_message_field.partner.request[9].response_chain_flag | json_a |
| mapped_message_field.partner.response[0].response_chain_flag | json_a |
| mapped_message_field.partner.response[10].response_chain_flag | json_a |
| mapped_message_field.partner.response[11].response_chain_flag | json_a |
| mapped_message_field.partner.response[12].response_chain_flag | json_a |
| mapped_message_field.partner.response[13].response_chain_flag | json_a |
| mapped_message_field.partner.response[14].response_chain_flag | json_a |
| mapped_message_field.partner.response[1].response_chain_flag | json_a |
| mapped_message_field.partner.response[2].response_chain_flag | json_a |
| mapped_message_field.partner.response[3].response_chain_flag | json_a |
| mapped_message_field.partner.response[4].response_chain_flag | json_a |
| mapped_message_field.partner.response[5].response_chain_flag | json_a |
| mapped_message_field.partner.response[6].response_chain_flag | json_a |
| mapped_message_field.partner.response[7].response_chain_flag | json_a |
| mapped_message_field.partner.response[8].response_chain_flag | json_a |
| mapped_message_field.partner.response[9].response_chain_flag | json_a |
| response_code.flag.sensitive_field_flag | json_a |
| transaction_record_mapping.currency_field_name | json_a |

## Annotated json_a
> **Legend**: <span style='background-color: #ffe6e6; color: #cc0000; font-weight: bold;'>Red Value</span> = Mismatch, <span style='background-color: #fff8e1; color: #e6a800; font-weight: bold;'>Orange Key</span> = Only in A

<pre><code>
{
    <span>"mst_service"</span>: {
        <span>"service_id"</span>: <span>"SVC025"</span>,
        <span>"service_name"</span>: <span>"pulsa-indosat"</span>
    },
    <span>"mst_category"</span>: {
        <span>"category_id"</span>: <span>"CTG018"</span>,
        <span>"category_name"</span>: <span>"PULSA"</span>
    },
    <span>"mst_product"</span>: {
        <span>"product_id"</span>: <span>"PRD012"</span>,
        <span>"product_name"</span>: <span>"MPO"</span>
    },
    <span>"mst_partner"</span>: {
        <span>"partner_id"</span>: <span>"PRT020"</span>,
        <span>"partner_name"</span>: <span>"Restswitching"</span>,
        <span>"fee"</span>: <span>"0.00"</span>,
        <span>"base_url"</span>: <span>"https://pegadaianrestswitching-dev-integration-switching-dev.apps.ocp-dev.pegadaian.co.id"</span>
    },
    <span>"flow_setup"</span>: {
        <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
        <span>"flow_setup_name"</span>: <span>"payment-pulsa-indosat"</span>,
        <span>"flow_constructor"</span>: [
            <span>"targetPartner:success>complete"</span>,
            <span>"targetPartner:default>end"</span>
        ],
        <span>"transaction_flag"</span>: <span>1</span>,
        <span>"is_callback"</span>: <span>0</span>
    },
    <span>"linkage_service_partner"</span>: {
        <span>"mapping_service_partner_id"</span>: <span>"MSP042"</span>,
        <span>"service_id"</span>: <span>"SVC025"</span>,
        <span>"partner_id"</span>: <span>"PRT020"</span>,
        <span>"sub_service_id"</span>: <span>""</span>,
        <span>"weight"</span>: <span>"100.00"</span>
    },
    <span>"mapping_service_integration"</span>: [],
    <span>"touchpoint"</span>: {
        <span>"touchpoint_id"</span>: <span>"TCP059"</span>,
        <span>"url"</span>: <span>"{{url}}/mpo/pulsa-indosat/payment-pulsa-indosat"</span>,
        <span>"kafka_topic"</span>: <span>"payvolution_payment-engine_mpo_pulsa-indosat_payment-pulsa-indosat"</span>,
        <span>"message_type"</span>: <span>null</span>
    },
    <span>"connector_config_integration"</span>: [],
    <span>"connector_config_channel"</span>: {
        <span>"channel_id_field_name"</span>: <span>null</span>,
        <span>"channel_id_field_location"</span>: <span>null</span>,
        <span>"channel_list"</span>: []
    },
    <span>"connector_config"</span>: {
        <span>"partner"</span>: {
            <span>"connector_config_id"</span>: <span>"CON017"</span>,
            <span>"connector_type"</span>: <span>"http"</span>,
            <span>"base_endpoint"</span>: <span>"https://pegadaianrestswitching-qa-regresi-switching-dev.apps.ocp-dev.pegadaian.co.id"</span>,
            <span>"connector_name"</span>: <span>"Restswitching Connector"</span>,
            <span>"auth_type"</span>: <span>"basic_auth"</span>,
            <span>"auth_path"</span>: <span>""</span>,
            <span>"credential_val"</span>: <span>"username=9977|password=PDSpGd123!"</span>,
            <span>"signature_source"</span>: <span>null</span>,
            <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"connection_time_out"</span>: <span style="background-color: #fff8e1; color: #e6a800;">null</span>,
            <span>"token"</span>: []
        }
    },
    <span>"connector_config_external_signature"</span>: {},
    <span>"mapped_message_field"</span>: {
        <span>"partner"</span>: {
            <span>"request"</span>: [
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"administrasi"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF001"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"administrasi"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD001"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"amount"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF002"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"amount"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD002"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"channelId"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF003"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"channelId"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD003"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"clientId"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF004"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"clientId"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD004"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"flag"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF005"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"flag"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD006"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>"argument|val=seluler"</span>,
                    <span>"message_partner_field"</span>: <span>"group"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF006"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>""</span>,
                    <span>"message_field_id"</span>: <span>""</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>null</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>"argument|val=MP"</span>,
                    <span>"message_partner_field"</span>: <span>"jenisTransaksi"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF007"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>""</span>,
                    <span>"message_field_id"</span>: <span>""</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>null</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"kodeBiller"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF008"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"kodeBiller"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD007"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"kodeLayananMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF009"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"kodeLayananMpo"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD008"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"norek"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF010"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"denom"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD005"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"reffBiller"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF011"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"reffBiller"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD011"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"reffSwitching"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF012"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"reffSwitching"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD012"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>"argument|val=BANK"</span>,
                    <span>"message_partner_field"</span>: <span>"paymentMethod"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF013"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>""</span>,
                    <span>"message_field_id"</span>: <span>""</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>null</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>"argument|val=002"</span>,
                    <span>"message_partner_field"</span>: <span>"kodeBankPembayar"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF014"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>""</span>,
                    <span>"message_field_id"</span>: <span>""</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>null</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                }
            ],
            <span>"response"</span>: [
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>norek"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF008"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>noHp"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD019"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"responseDesc"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF002"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"responseDesc"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD014"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>kodeBiller"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF006"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>kodeBiller"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD016"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>kodeLayananMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF007"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>kodeLayananMpo"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD017"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>reffSwitching"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF013"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>reffSwitching"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD020"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>tglTransaksi"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF014"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>tglTransaksi"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD022"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>totalKewajiban"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF015"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>totalKewajiban"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD023"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>reffBiller"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF009"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>reffBiller"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD024"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>reffMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF010"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>reffMpo"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD026"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>sid"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF004"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>sid"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD027"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>respCodeMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF011"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>responseCodeNative"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD029"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>respDescMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF012"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>responseDescNative"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD030"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>serialNumber"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF003"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>serialNumber"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD031"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"responseCode"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF001"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"responseCode"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD013"</span>,
                    <span>"response_code_flag"</span>: <span>1</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>norek"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF008"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>noHp"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD028"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>,
                    <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"response_chain_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
                }
            ]
        }
    },
    <span>"mapped_message_field_integration"</span>: [],
    <span>"parameter_management"</span>: [],
    <span>"response_code"</span>: {
        <span>"flag"</span>: {
            <span>"message_field_id"</span>: <span>"MSG089FLD013"</span>,
            <span>"standar_message_setup_id"</span>: <span>"MSG089"</span>,
            <span>"message_field"</span>: <span>"responseCode"</span>,
            <span>"location"</span>: <span>"body"</span>,
            <span>"response_code_flag"</span>: <span>1</span>,
            <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"sensitive_field_flag"</span>: <span style="background-color: #fff8e1; color: #e6a800;">0</span>
        },
        <span>"mapped"</span>: [
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM217"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC150"</span>,
                <span>"response_code_ori"</span>: <span>"12"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP160"</span>,
                <span>"response_code"</span>: <span>"4000011912"</span>,
                <span>"response_desc"</span>: <span>"Invalid transaction"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM218"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC149"</span>,
                <span>"response_code_ori"</span>: <span>"13"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP161"</span>,
                <span>"response_code"</span>: <span>"4220011913"</span>,
                <span>"response_desc"</span>: <span>"Jumlah tidak sesuai"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM219"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC148"</span>,
                <span>"response_code_ori"</span>: <span>"14"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP162"</span>,
                <span>"response_code"</span>: <span>"4040011914"</span>,
                <span>"response_desc"</span>: <span>"Rekening/Data tidak ditemukan"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM220"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC147"</span>,
                <span>"response_code_ori"</span>: <span>"15"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP163"</span>,
                <span>"response_code"</span>: <span>"4030011915"</span>,
                <span>"response_desc"</span>: <span>"Rekening Blokir / Tidak Aktif"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM221"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC146"</span>,
                <span>"response_code_ori"</span>: <span>"16"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP164"</span>,
                <span>"response_code"</span>: <span>"4030011916"</span>,
                <span>"response_desc"</span>: <span>"CIF Sudah tidak aktif"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM223"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC145"</span>,
                <span>"response_code_ori"</span>: <span>"17"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP165"</span>,
                <span>"response_code"</span>: <span>"4040011917"</span>,
                <span>"response_desc"</span>: <span>"Param Not Found"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM106"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC105"</span>,
                <span>"response_code_ori"</span>: <span>"00"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP120"</span>,
                <span>"response_code"</span>: <span>"2000011900"</span>,
                <span>"response_desc"</span>: <span>"Approved"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM214"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC153"</span>,
                <span>"response_code_ori"</span>: <span>"0X"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP157"</span>,
                <span>"response_code"</span>: <span>"400001190X"</span>,
                <span>"response_desc"</span>: <span>"Failed"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM215"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC152"</span>,
                <span>"response_code_ori"</span>: <span>"X4"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP158"</span>,
                <span>"response_code"</span>: <span>"40400119X4"</span>,
                <span>"response_desc"</span>: <span>"There is no resource path"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM216"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC151"</span>,
                <span>"response_code_ori"</span>: <span>"X5"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP159"</span>,
                <span>"response_code"</span>: <span>"50000119X5"</span>,
                <span>"response_desc"</span>: <span>"Service internal error"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM222"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC144"</span>,
                <span>"response_code_ori"</span>: <span>"30"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP166"</span>,
                <span>"response_code"</span>: <span>"4000011930"</span>,
                <span>"response_desc"</span>: <span>"Format Data Salah"</span>
            }
        ],
        <span>"group"</span>: [
            {
                <span>"response_group_id"</span>: <span>"RSG059"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_group_name"</span>: <span>"success"</span>,
                <span>"deletable"</span>: <span>0</span>,
                <span>"response_group_details"</span>: [
                    {
                        <span>"response_group_detail_id"</span>: <span>"RGD016"</span>,
                        <span>"response_code_partner_id"</span>: <span>"RCP120"</span>,
                        <span>"response_code_ori"</span>: <span>"00"</span>
                    }
                ]
            }
        ]
    },
    <span>"response_code_integration"</span>: [],
    <span>"callback"</span>: {},
    <span>"message_management"</span>: {
        <span>"partner"</span>: {
            <span>"request"</span>: {
                <span>"partner_message_id"</span>: <span>"PMM085"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"message_type"</span>: <span>0</span>,
                <span>"api_method"</span>: <span>"post"</span>,
                <span>"url_path"</span>: <span>"mpo/posting/direct/mitra"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>
            },
            <span>"response"</span>: {
                <span>"partner_message_id"</span>: <span>"PMM086"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"message_type"</span>: <span>1</span>,
                <span>"api_method"</span>: <span>"post"</span>,
                <span>"url_path"</span>: <span>null</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>
            }
        }
    },
    <span>"message_management_integration"</span>: [],
    <span>"transaction_record_mapping"</span>: {
        <span>"transaction_record_mapping_id"</span>: <span>"TRM006"</span>,
        <span>"service_id"</span>: <span>"SVC025"</span>,
        <span>"step"</span>: <span>"FLW029"</span>,
        <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
        <span>"trx_id"</span>: <span>"MSG088FLD012"</span>,
        <span>"trx_id_field_name"</span>: <span>"reffSwitching"</span>,
        <span>"customer_id"</span>: <span>"MSG088FLD010"</span>,
        <span>"customer_id_field_name"</span>: <span>"noHp"</span>,
        <span>"amount"</span>: <span>"MSG088FLD002"</span>,
        <span>"amount_field_name"</span>: <span>"amount"</span>,
        <span>"currency"</span>: <span>null</span>,
        <span style="background-color: #fff8e1; color: #e6a800; font-weight: bold;">"currency_field_name"</span>: <span style="background-color: #fff8e1; color: #e6a800;">null</span>
    },
    <span>"sensitive_field"</span>: {
        <span>"standard"</span>: {
            <span>"request"</span>: [],
            <span>"response"</span>: []
        },
        <span>"partner"</span>: {
            <span>"request"</span>: [],
            <span>"response"</span>: [],
            <span>"integration"</span>: []
        }
    }
}
</code></pre>

## Annotated json_b
> **Legend**: <span style='background-color: #ffe6e6; color: #cc0000; font-weight: bold;'>Red Value</span> = Mismatch, <span style='background-color: #fff8e1; color: #e6a800; font-weight: bold;'>Orange Key</span> = Only in B

<pre><code>
{
    <span>"mst_service"</span>: {
        <span>"service_id"</span>: <span>"SVC025"</span>,
        <span>"service_name"</span>: <span>"pulsa-indosat"</span>
    },
    <span>"mst_category"</span>: {
        <span>"category_id"</span>: <span>"CTG018"</span>,
        <span>"category_name"</span>: <span>"PULSA"</span>
    },
    <span>"mst_product"</span>: {
        <span>"product_id"</span>: <span>"PRD012"</span>,
        <span>"product_name"</span>: <span>"MPO"</span>
    },
    <span>"mst_partner"</span>: {
        <span>"partner_id"</span>: <span>"PRT020"</span>,
        <span>"partner_name"</span>: <span>"Restswitching"</span>,
        <span>"fee"</span>: <span>"0.00"</span>,
        <span>"base_url"</span>: <span>"https://pegadaianrestswitching-dev-integration-switching-dev.apps.ocp-dev.pegadaian.co.id"</span>
    },
    <span>"flow_setup"</span>: {
        <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
        <span>"flow_setup_name"</span>: <span>"payment-pulsa-indosat"</span>,
        <span>"flow_constructor"</span>: [
            <span>"targetPartner:success>complete"</span>,
            <span>"targetPartner:default>end"</span>
        ],
        <span>"transaction_flag"</span>: <span>1</span>,
        <span>"is_callback"</span>: <span>0</span>
    },
    <span>"linkage_service_partner"</span>: {
        <span>"mapping_service_partner_id"</span>: <span>"MSP042"</span>,
        <span>"service_id"</span>: <span>"SVC025"</span>,
        <span>"partner_id"</span>: <span>"PRT020"</span>,
        <span>"sub_service_id"</span>: <span>""</span>,
        <span>"weight"</span>: <span>"100.00"</span>
    },
    <span>"mapping_service_integration"</span>: [],
    <span>"touchpoint"</span>: {
        <span>"touchpoint_id"</span>: <span>"TCP059"</span>,
        <span>"url"</span>: <span>"{{url}}/mpo/pulsa-indosat/payment-pulsa-indosat"</span>,
        <span>"kafka_topic"</span>: <span>"payvolution_payment-engine_mpo_pulsa-indosat_payment-pulsa-indosat"</span>,
        <span>"message_type"</span>: <span>null</span>
    },
    <span>"connector_config_integration"</span>: [],
    <span>"connector_config_channel"</span>: {
        <span>"channel_id_field_name"</span>: <span>null</span>,
        <span>"channel_id_field_location"</span>: <span>null</span>,
        <span>"channel_list"</span>: []
    },
    <span>"connector_config"</span>: {
        <span>"partner"</span>: {
            <span>"connector_config_id"</span>: <span>"CON017"</span>,
            <span>"connector_type"</span>: <span>"http"</span>,
            <span>"base_endpoint"</span>: <span>"https://pegadaianrestswitching-qa-regresi-switching-dev.apps.ocp-dev.pegadaian.co.id"</span>,
            <span>"connector_name"</span>: <span>"Restswitching Connector"</span>,
            <span>"auth_type"</span>: <span>"basic_auth"</span>,
            <span>"auth_path"</span>: <span>""</span>,
            <span>"credential_val"</span>: <span>"username=9977|password=PDSpGd123!"</span>,
            <span>"signature_source"</span>: <span>null</span>,
            <span>"token"</span>: []
        }
    },
    <span>"connector_config_external_signature"</span>: {},
    <span>"mapped_message_field"</span>: {
        <span>"partner"</span>: {
            <span>"request"</span>: [
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"administrasi"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF001"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"administrasi"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD001"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"amount"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF002"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"amount"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD002"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"channelId"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF003"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"channelId"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD003"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"clientId"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF004"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"clientId"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD004"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"flag"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF005"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"flag"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD006"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>"argument|val=seluler"</span>,
                    <span>"message_partner_field"</span>: <span>"group"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF006"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>""</span>,
                    <span>"message_field_id"</span>: <span>""</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>null</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>"argument|val=MP"</span>,
                    <span>"message_partner_field"</span>: <span>"jenisTransaksi"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF007"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>""</span>,
                    <span>"message_field_id"</span>: <span>""</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>null</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"kodeBiller"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF008"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"kodeBiller"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD007"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"kodeLayananMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF009"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"kodeLayananMpo"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD008"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"norek"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF010"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"denom"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD005"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"reffBiller"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF011"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"reffBiller"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD011"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"reffSwitching"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF012"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"reffSwitching"</span>,
                    <span>"message_field_id"</span>: <span>"MSG088FLD012"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>"argument|val=BANK"</span>,
                    <span>"message_partner_field"</span>: <span>"paymentMethod"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF013"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>""</span>,
                    <span>"message_field_id"</span>: <span>""</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>null</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>"argument|val=002"</span>,
                    <span>"message_partner_field"</span>: <span>"kodeBankPembayar"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM085MPF014"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>""</span>,
                    <span>"message_field_id"</span>: <span>""</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>null</span>,
                    <span>"value"</span>: <span>null</span>
                }
            ],
            <span>"response"</span>: [
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>norek"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF008"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>noHp"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD019"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"responseDesc"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF002"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"responseDesc"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD014"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>kodeBiller"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF006"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>kodeBiller"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD016"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>kodeLayananMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF007"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>kodeLayananMpo"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD017"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>reffSwitching"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF013"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>reffSwitching"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD020"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>tglTransaksi"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF014"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>tglTransaksi"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD022"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>totalKewajiban"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF015"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>totalKewajiban"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD023"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>reffBiller"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF009"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>reffBiller"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD024"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>reffMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF010"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>reffMpo"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD026"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>sid"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF004"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>sid"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD027"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>respCodeMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF011"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>responseCodeNative"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD029"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>respDescMpo"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF012"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>responseDescNative"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD030"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>serialNumber"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF003"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>serialNumber"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD031"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"responseCode"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF001"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"responseCode"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD013"</span>,
                    <span>"response_code_flag"</span>: <span>1</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                },
                {
                    <span>"transform_arg"</span>: <span>null</span>,
                    <span>"message_partner_field"</span>: <span>"data>norek"</span>,
                    <span>"message_partner_field_id"</span>: <span>"PMM086MPF008"</span>,
                    <span>"callback_flag"</span>: <span>0</span>,
                    <span>"message_partner_field_location"</span>: <span>"body"</span>,
                    <span>"message_field"</span>: <span>"data>dataMpo>noHp"</span>,
                    <span>"message_field_id"</span>: <span>"MSG089FLD028"</span>,
                    <span>"response_code_flag"</span>: <span>0</span>,
                    <span>"message_field_location"</span>: <span>"body"</span>,
                    <span>"value"</span>: <span>null</span>
                }
            ]
        }
    },
    <span>"mapped_message_field_integration"</span>: [],
    <span>"parameter_management"</span>: [],
    <span>"response_code"</span>: {
        <span>"flag"</span>: {
            <span>"message_field_id"</span>: <span>"MSG089FLD013"</span>,
            <span>"standar_message_setup_id"</span>: <span>"MSG089"</span>,
            <span>"message_field"</span>: <span>"responseCode"</span>,
            <span>"location"</span>: <span>"body"</span>,
            <span>"response_code_flag"</span>: <span>1</span>
        },
        <span>"mapped"</span>: [
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM217"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC150"</span>,
                <span>"response_code_ori"</span>: <span>"12"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP160"</span>,
                <span>"response_code"</span>: <span>"4000011912"</span>,
                <span>"response_desc"</span>: <span>"Invalid transaction"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM218"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC149"</span>,
                <span>"response_code_ori"</span>: <span>"13"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP161"</span>,
                <span>"response_code"</span>: <span>"4220011913"</span>,
                <span>"response_desc"</span>: <span>"Jumlah tidak sesuai"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM219"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC148"</span>,
                <span>"response_code_ori"</span>: <span>"14"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP162"</span>,
                <span>"response_code"</span>: <span>"4040011914"</span>,
                <span>"response_desc"</span>: <span>"Rekening/Data tidak ditemukan"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM220"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC147"</span>,
                <span>"response_code_ori"</span>: <span>"15"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP163"</span>,
                <span>"response_code"</span>: <span>"4030011915"</span>,
                <span>"response_desc"</span>: <span>"Rekening Blokir / Tidak Aktif"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM221"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC146"</span>,
                <span>"response_code_ori"</span>: <span>"16"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP164"</span>,
                <span>"response_code"</span>: <span>"4030011916"</span>,
                <span>"response_desc"</span>: <span>"CIF Sudah tidak aktif"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM223"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC145"</span>,
                <span>"response_code_ori"</span>: <span>"17"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP165"</span>,
                <span>"response_code"</span>: <span>"4040011917"</span>,
                <span>"response_desc"</span>: <span>"Param Not Found"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM106"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC105"</span>,
                <span>"response_code_ori"</span>: <span>"00"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP120"</span>,
                <span>"response_code"</span>: <span>"2000011900"</span>,
                <span>"response_desc"</span>: <span>"Approved"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM214"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC153"</span>,
                <span>"response_code_ori"</span>: <span>"0X"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP157"</span>,
                <span>"response_code"</span>: <span>"400001190X"</span>,
                <span>"response_desc"</span>: <span>"Failed"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM215"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC152"</span>,
                <span>"response_code_ori"</span>: <span>"X4"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP158"</span>,
                <span>"response_code"</span>: <span>"40400119X4"</span>,
                <span>"response_desc"</span>: <span>"There is no resource path"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM216"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC151"</span>,
                <span>"response_code_ori"</span>: <span>"X5"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP159"</span>,
                <span>"response_code"</span>: <span>"50000119X5"</span>,
                <span>"response_desc"</span>: <span>"Service internal error"</span>
            },
            {
                <span>"response_code_mapper_id"</span>: <span>"RCM222"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_code_id"</span>: <span>"RSC144"</span>,
                <span>"response_code_ori"</span>: <span>"30"</span>,
                <span>"response_code_partner_id"</span>: <span>"RCP166"</span>,
                <span>"response_code"</span>: <span>"4000011930"</span>,
                <span>"response_desc"</span>: <span>"Format Data Salah"</span>
            }
        ],
        <span>"group"</span>: [
            {
                <span>"response_group_id"</span>: <span>"RSG059"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
                <span>"response_group_name"</span>: <span>"success"</span>,
                <span>"deletable"</span>: <span>0</span>,
                <span>"response_group_details"</span>: [
                    {
                        <span>"response_group_detail_id"</span>: <span>"RGD016"</span>,
                        <span>"response_code_partner_id"</span>: <span>"RCP120"</span>,
                        <span>"response_code_ori"</span>: <span>"00"</span>
                    }
                ]
            }
        ]
    },
    <span>"response_code_integration"</span>: [],
    <span>"callback"</span>: {},
    <span>"message_management"</span>: {
        <span>"partner"</span>: {
            <span>"request"</span>: {
                <span>"partner_message_id"</span>: <span>"PMM085"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"message_type"</span>: <span>0</span>,
                <span>"api_method"</span>: <span>"post"</span>,
                <span>"url_path"</span>: <span>"mpo/posting/direct/mitra"</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>
            },
            <span>"response"</span>: {
                <span>"partner_message_id"</span>: <span>"PMM086"</span>,
                <span>"service_id"</span>: <span>"SVC025"</span>,
                <span>"partner_id"</span>: <span>"PRT020"</span>,
                <span>"step"</span>: <span>"FLW029"</span>,
                <span>"message_type"</span>: <span>1</span>,
                <span>"api_method"</span>: <span>"post"</span>,
                <span>"url_path"</span>: <span>null</span>,
                <span>"flow_setup_id"</span>: <span>"FLW029"</span>
            }
        }
    },
    <span>"message_management_integration"</span>: [],
    <span>"transaction_record_mapping"</span>: {
        <span>"transaction_record_mapping_id"</span>: <span>"TRM006"</span>,
        <span>"service_id"</span>: <span>"SVC025"</span>,
        <span>"step"</span>: <span>"FLW029"</span>,
        <span>"flow_setup_id"</span>: <span>"FLW029"</span>,
        <span>"trx_id"</span>: <span>"MSG088FLD012"</span>,
        <span>"trx_id_field_name"</span>: <span>"reffSwitching"</span>,
        <span>"customer_id"</span>: <span>"MSG088FLD010"</span>,
        <span>"customer_id_field_name"</span>: <span>"noHp"</span>,
        <span>"amount"</span>: <span>"MSG088FLD002"</span>,
        <span>"amount_field_name"</span>: <span>"amount"</span>,
        <span>"currency"</span>: <span>null</span>
    }
}
</code></pre>
