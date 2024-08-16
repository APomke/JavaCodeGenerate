entity_template_str = """
package {{ package_name }}.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class {{ class_name }} {
    /**
    * @author admin
    * @version 1.0
    * @Description 实体类
    */
    {% for attributes in table_structure %}
    private {{ attributes.attributesType }} {{ attributes.attributesName }};
    {%- endfor %}
}
"""
