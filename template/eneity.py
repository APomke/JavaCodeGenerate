entity_template_str = """
package {{ packageName }};

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class {{className}} {
    /**
    * @author admin
    * @version 1.0
    * @Description 实体类
    */
    {% for attributes in tableStructure %}
    private {{ attributes.attributesType }} {{ attributes.attributesName }};
    {%- endfor %}
}
"""
