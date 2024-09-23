controller_template_str = """
package {{ package_name }}.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import {{ package_name }}.entity.{{ entity_name }};
import {{ package_name }}.service.{{ service_name }};
import {{ package_name }}.entity.ResponseVO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@RestController
public class {{ entity_name }}Controller {

    @Autowired
    private {{ entity_name }}Service {{ entity_name | lower }}Service;
    
    // 查询
    {% for entity in entity_list %}
    {% if entity.name == 'id' %}
    @GetMapping("/get{{ entity_name }}ListBy{{ entity.name_first }}")
    public ResponseVO get{{ entity_name }}By{{ entity.name_first }}({{ entity.type }} {{ entity.name }}) {
        ResponseVO responseVO = new ResponseVO();
        
        {{ entity_name }} {{ entity_name | lower }}List = {{ entity_name | lower }}Service.get{{ entity_name }}By{{ entity.name_first }}({{ entity.name }});
        responseVO.setCode(200);
        responseVO.setInfo("查询成功！");
        responseVO.setStatus("success");
        responseVO.setData({{ entity_name | lower }}List);
        return responseVO;
    }
    {% else %}
    @GetMapping("/get{{ entity_name }}ListBy{{ entity.name_first }}")
    public ResponseVO get{{ entity_name }}ListBy{{ entity.name_first }}({{ entity.type }} {{ entity.name }}) {
        ResponseVO responseVO = new ResponseVO();
        
        List<{{ entity_name }}> {{ entity_name | lower }}List = {{ entity_name | lower }}Service.get{{ entity_name }}ListBy{{ entity.name_first }}({{ entity.name }});
        responseVO.setCode(200);
        responseVO.setInfo("查询成功！");
        responseVO.setStatus("success");
        responseVO.setData({{ entity_name | lower }}List);
        return responseVO;
    }
    {% endif %}
    {%- endfor %}
    
    // 修改
    @PostMapping("/update{{ entity_name }}")
    public ResponseVO update{{ entity_name }}({{ entity_name }} {{ entity_name | lower }}) {
        ResponseVO responseVO = new ResponseVO();
        int i = {{ entity_name | lower }}Service.update{{ entity_name }}({{ entity_name | lower }});
        responseVO.setCode(200);
        responseVO.setInfo("修改成功！");
        responseVO.setStatus("success");
        return responseVO;
        
    }
    // 增加
    @PostMapping("/add{{ entity_name }}")
    public ResponseVO add{{ entity_name }}({{ entity_name }} {{ entity_name | lower }}) {
        ResponseVO responseVO = new ResponseVO();
        int i = {{ entity_name | lower }}Service.add{{ entity_name }}({{ entity_name | lower }});
        responseVO.setCode(200);
        responseVO.setInfo("增加成功！");
        responseVO.setStatus("success");
        return responseVO;
    }
    // 删除
    @PostMapping("/delete{{ entity_name }}")
    public ResponseVO delete{{ entity_name }}({{ entity_name }} {{ entity_name | lower }}) {
        ResponseVO responseVO = new ResponseVO();
        int i = {{ entity_name | lower }}Service.delete{{ entity_name }}({{ entity_name | lower }}.getId());
        responseVO.setCode(200);
        responseVO.setInfo("删除成功！");
        responseVO.setStatus("success");
        return responseVO;
    }
    
}

"""